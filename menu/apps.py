# * coding: UTF-8
try:
    from django.apps import AppConfig

    class AppConfig(AppConfig):
        name = 'menu'
        verbose_name = u"Меню"
except ImportError:
    pass