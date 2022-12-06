from django.contrib import admin
from . import models


class BranchAdmin(admin.ModelAdmin):
    list_display = ('get_formatted', )
    list_filter = ('parent', )

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('get_formatted', 'level', 'base_cost', 'rarity', )
    list_filter = ('branch', 'level', )


admin.site.register(models.Branch, BranchAdmin)
admin.site.register(models.Technology, TechnologyAdmin)
admin.site.register(models.Dependency)
admin.site.register(models.Catalyst)
