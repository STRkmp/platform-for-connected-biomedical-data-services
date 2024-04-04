from configparser import RawConfigParser, ExtendedInterpolation
from qmanager.qmanager_config import QManagerSettings


app_config = RawConfigParser(interpolation=ExtendedInterpolation())
app_config.read('application.ini')


Settings = QManagerSettings.parse_obj(app_config['QueueManager'])
Workers = 2
