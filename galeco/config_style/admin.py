from django.contrib import admin
from . import models


class ColorAdmin(admin.ModelAdmin):
    list_display = ('display_sample', 'html_code', 'red', 'green', 'blue', 'alpha', )
    list_display_links = ('display_sample', )
    list_filter = (
        'used_for_tech_categories',
        'used_for_logo_designs',
        'used_for_ui_schemes',
        'used_as_main_system',
    )
    fieldsets = (
        ('Color', {
            "fields": (
                ('red', 'green', 'blue', 'alpha', 'html_code'),
            ),
        }),
        ('General', {
            "fields": (
                'name',
            )
        }),
        ('Usage', {
            "fields": (
                'used_for_tech_categories',
                'used_for_logo_designs',
                'used_for_ui_schemes',
                'used_as_main_system',
            )
        })
    )


admin.site.register(models.Color, ColorAdmin)
