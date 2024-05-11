from qmanager.qmanager_config import QManagerSettings
import os


# Создаем объект настроек для QueueManager, используя переменные окружения с префиксом QUEUE_MANAGER
Settings = QManagerSettings(
    queue_type=os.getenv('QUEUE_TYPE', 'KOMBU_RMQ'),
    host=os.getenv('RABBITMQ_HOST', 'localhost'),
    port=int(os.getenv('RABBITMQ_PORT', '5672')),
    virtual_host=os.getenv('RABBITMQ_VIRTUAL_HOST', '/'),
    exchange=os.getenv('RABBITMQ_EXCHANGE', 'platform'),
    username=os.getenv('RABBITMQ_USER', 'guest'),
    password=os.getenv('RABBITMQ_PASS', 'guest'),
    auto_ack=os.getenv('AUTO_ACK', True),
    queue_in=os.getenv('QUEUE_IN', 'processing_model1'), # Имя сервиса Diabet_sldkfjsdf_recognize
    queue_out=os.getenv('QUEUE_OUT', 'ResultFromServiceMessage'),
    queue_err=os.getenv('QUEUE_ERR', 'ReqeustForServiceResultError'),
    queue_timeout=int(os.getenv('QUEUE_TIMEOUT', '10')))

Workers = 1
