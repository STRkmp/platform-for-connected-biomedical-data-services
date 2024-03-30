from configparser import ConfigParser, RawConfigParser, ExtendedInterpolation
from qmanager.qmanager_config import QManagerSettings
from qmanager.qmanager_factory import QueueManagerFactory
import os

# Получаем путь к текущей директории
current_directory = os.path.dirname(__file__)

# Формируем относительный путь к файлу application.ini
relative_path = 'application.ini'

# Получаем абсолютный путь к файлу application.ini
absolute_path = os.path.abspath(os.path.join(current_directory, relative_path))

# Инициализируем объект конфигурации
app_config = RawConfigParser(interpolation=ExtendedInterpolation())

# Читаем файл конфигурации, передавая абсолютный путь
app_config.read(absolute_path)

Settings = QManagerSettings.parse_obj(app_config['QueueManager'])
Workers = 2
