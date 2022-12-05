from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConfigStyleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config_style'
    verbose_name = _('config style')
