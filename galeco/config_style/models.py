from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class Color(models.Model):
    html_code = models.CharField(_("HTML code"), max_length=7, blank=True, db_index=True, unique=True)
    red = models.PositiveSmallIntegerField(_("red"), default=0)
    green = models.PositiveSmallIntegerField(_("green"), default=0)
    blue = models.PositiveSmallIntegerField(_("blue"), default=0)
    alpha = models.DecimalField(_("alpha"), max_digits=5, decimal_places=4, default=1)
    name = models.SlugField(_("name"), max_length=50, blank=True, null=True)

    used_as_main_system = models.BooleanField(_("Used as main system color"), default=False)
    used_for_ui_schemes = models.BooleanField(_("used for UI schemes"), default=False)
    used_for_tech_categories = models.BooleanField(_("used for technology categories"), default=False)
    used_for_logo_designs = models.BooleanField(_("used for logo designs"), default=True)

    class Meta:
        verbose_name = _("color")
        verbose_name_plural = _("colors")
        ordering = ('html_code', )

    def __str__(self) -> str:
        if self.name:
            return self.name
        return self.get_css()

    def get_html_code(self):
        return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

    def get_css_rgba(self):
        return f"rgba({self.red}, {self.green}, {self.blue}, {self.alpha})"

    def get_css(self):
        if self.alpha < 1:
            return self.get_css_rgba()
        else:
            return self.get_html_code()

    def save(self, *args, **kwargs):
        self.html_code = self.get_html_code()
        super().save(*args, **kwargs)

    def display_sample(self, width=16, height=16, text=None):
        return format_html(
            '<span style="background-color: {code}; border: 1px solid #000; '\
            'width: {width}px; height: {height}px; display: inline-block; '\
            'vertical-align: middle;"></span> {text}',
            code=self.get_html_code(),
            width=width, height=height,
            text=text or self.__str__(),
        )
    display_sample.short_description = _('color')
