from qmanager.qmanager_factory import QueueManagerFactory
from pydantic import BaseSettings
from .config import Settings, Workers
from threading import Thread
from common.utils.check_migrations import is_migrations
import jsonpickle

class ThreadedConsumer(Thread):
    def __init__(self, settings: BaseSettings):
        Thread.__init__(self)
        self.qmanager = QueueManagerFactory(settings).get_instance(callback_func=self.process_request)

    def run(self):
        print(f'{self.name} Consuming...')
        self.qmanager.consume()

    def process_request(self, data: bytes, headers: dict = None) -> None:
        from api.models import DiagnosisRequest
        from api.upload import save_to_db

        print(f'{self.name} RECEIVED {headers}\n{type(data)}\n{data}')

        result = jsonpickle.decode(data)
        request_id = result['request_id']
        status = result['status']

        try:
            request = DiagnosisRequest.objects.get(id=request_id)

            if status == 'success':
                uploaded_result = save_to_db(result['path_to_result'])
                print(f'{self.name} UPLOADED file')
                request.result_file = uploaded_result

            request.status = status
            request.save()

            print(f'{self.name} Handled request {request_id}')
        except DiagnosisRequest.DoesNotExist:
            print(f'Request with id {request_id} not found.')
        except Exception as e:
            print(f'{self.name} error {e}')


def start_consumer():
    if not is_migrations():
        for instance in range(Workers):
            print("запустил консьюмера {}".format(instance))
            ThreadedConsumer(Settings).start()
    else:
        print("Миграции. не подключаемся к реббиту")