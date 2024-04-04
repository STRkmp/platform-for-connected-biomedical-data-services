from qmanager.qmanager_config import QManagerSettings
import os

prefix = 'DJANGO_CONSUMER'

# Функция для чтения переменных окружения с учетом префикса
def getenv_with_prefix(prefix, key, default=None):
    return os.getenv(f'{prefix}_{key}', default)


# Создаем объект настроек для QueueManager, используя переменные окружения с префиксом QUEUE_MANAGER
Settings = QManagerSettings(
    queue_type=os.getenv('QUEUE_TYPE', 'KOMBU_RMQ'),
    host=os.getenv('RABBITMQ_HOST', 'rabbitmq'),
    port=int(os.getenv('RABBITMQ_PORT', '5672')),
    virtual_host=os.getenv('RABBITMQ_VIRTUAL_HOST', '5672'),
    exchange=os.getenv('RABBITMQ_EXCHANGE', 'platform'),
    username=os.getenv('RABBITMQ_USER', 'guest'),
    password=os.getenv('RABBITMQ_PASS', 'guest'),
    auto_ack=getenv_with_prefix(prefix, 'AUTO_ACK', True),
    queue_in=getenv_with_prefix(prefix, 'QUEUE_IN', 'ReqeustForServiceResult'),
    queue_out=getenv_with_prefix(prefix, 'QUEUE_OUT', ''),
    queue_err=getenv_with_prefix(prefix, 'QUEUE_ERR', 'ReqeustForServiceResultError'),
    queue_timeout=int(getenv_with_prefix(prefix, 'QUEUE_TIMEOUT', '10'))
)

Workers = 2
