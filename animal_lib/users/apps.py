from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "animal_lib.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import animal_lib.users.signals  # noqa F401
        except ImportError:
            pass
