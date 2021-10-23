#Используется для конфигурации всего приложения
from django.apps import AppConfig


class WomenConfig(AppConfig): #используется для конфигурации всего приложения Women
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
    verbose_name = 'Женщины мира'