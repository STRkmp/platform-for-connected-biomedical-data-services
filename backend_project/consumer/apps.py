from django.apps import AppConfig
from .consumer import start_consumer

class MyAppConfig(AppConfig):
    name = 'consumer'

    def ready(self):
        # Запуск функции потребителя при загрузке Django приложения
        start_consumer()
