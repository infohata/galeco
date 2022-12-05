from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class Branch(models.Model):
    name = models.CharField(_("name"), max_length=50)
    color = models.ForeignKey(
        "config_style.Color", 
        verbose_name=_("color"), 
        on_delete=models.DO_NOTHING, 
        to_field='html_code',
        related_name='tech_branches',
        default='#cccccc',
    )
    parent = models.ForeignKey(
        "Branch", 
        verbose_name=_("parent branch"), 
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = _("branch")
        verbose_name_plural = _("branches")

    def __str__(self) -> str:
        return self.name

    def get_formatted(self) -> str:
        return self.color.display_sample(text=self.name)
    get_formatted.short_description = 'tech branch'


class Technology(models.Model):
    name = models.CharField(_("name"), max_length=120)
    description = HTMLField(_("description"), max_length=4000)
    base_cost = models.PositiveSmallIntegerField(_("base cost"), default=1000, db_index=True)
    level = models.SmallIntegerField(_("level"), default=0)
    rarity = models.PositiveIntegerField(_("rarity"), default=100)
    starting = models.BooleanField(_("starting technology"), default=False)
    branch = models.ForeignKey(
        Branch, 
        verbose_name=_("branch"), 
        on_delete=models.CASCADE,
        related_name='technologies',
    )

    class Meta:
        ordering = ('base_cost', 'rarity', 'id',)
        verbose_name = _("technology")
        verbose_name_plural = _("technologies")

    def __str__(self) -> str:
        return self.name

    def get_formatted(self) -> str:
        return self.branch.color.display_sample(text=self.name)
    get_formatted.short_description = 'technology'



class Dependency(models.Model):
    target_technology = models.ForeignKey(
        Technology, 
        verbose_name=_("target technology"), 
        on_delete=models.CASCADE,
        related_name='dependencies',
    )
    dependency = models.ForeignKey(
        Technology, 
        verbose_name=_("depends on"), 
        on_delete=models.CASCADE,
        related_name='leads',
    )

    class Meta:
        ordering = ('target_technology', 'dependency',)
        verbose_name = _("dependency")
        verbose_name_plural = _("dependencies")

    def __str__(self) -> str:
        return f"{self.target_technology} {_('depends on')} {self.dependency}"
    
    def get_formatted(self):
        return f"{self.target_technology.get_formatted()} {_('depends on')} {self.dependency.get_formatted()}"


class Catalyst(models.Model):
    technology = models.ForeignKey(
        Technology, 
        verbose_name=_("technology"), 
        on_delete=models.CASCADE,
        related_name='catalysts',
    )
    # TODO: link when implementing events app
    event = models.CharField(_("event"), max_length=250, blank=True, null=True)
    rarity_base_modifier = models.IntegerField(_("rarity base modifier"), default=0)
    rarity_divisive_modifier = models.DecimalField(_("rarity divisive modifier"), max_digits=5, decimal_places=4, default=1)

    class Meta:
        ordering = ('technology', 'id',)
        verbose_name = _("catalyst")
        verbose_name_plural = _("catalysts")
