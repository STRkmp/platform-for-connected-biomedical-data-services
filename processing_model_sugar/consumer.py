from qmanager.qmanager_factory import QueueManagerFactory
from pydantic import BaseSettings
import jsonpickle
from common.utils.minio_utils import get_object_from_minio, upload_to_minio, replace_path_file
from common.dto.ResultFromServiceMessage import ResultFromServiceMessage
from recognize_core import recognize


class Consumer:
    def __init__(self, settings: BaseSettings):
        self.qmanager = QueueManagerFactory(settings).get_instance(callback_func=self.process_request)

    def run(self):
        print(f'{self} Consuming...')
        self.qmanager.consume()

    # Необходимо переназначить этот метод
    def process_request(self, data: bytes, headers: dict = None) -> None:
        try:
            print(f'RECEIVED {headers}\n{type(data)}\n{data}')
            request = jsonpickle.decode(data)
            file = get_object_from_minio(request['path_to_file'])
            if file is None:
                raise Exception('No file found. Request : {}'.format(request))

            created_file = recognize(file)  # тут файл сформированный         ##ТУТ НУЖНО ВЫЗВАТЬ СВОЙ МЕТОД ДЛЯ ОБРАБОТКИ ФАЙЛА, ЧТОБЫ ОН ВОЗВРАЩАЛ СФОРМИРОВАННЫЙ НОВЫЙ ФАЙЛ С ИМЕНЕМ RESULT (.HTML ИЛИ .PDF) и возможно описание

            path = replace_path_file(request['path_to_file'],
                                     created_file.name)  # подставить имя нового файла, вместо "Result.pdf" file.name

            upload_to_minio(path, created_file)

            result = ResultFromServiceMessage(
                request_id=request['request_id'],
                path_to_result=path,
                status='success'
            )
            self.send_result(result)

        except Exception as e:
            print(f'Получили ошибку: {e}')
            result = ResultFromServiceMessage(
                request_id=request['request_id'],
                status='error'
            )
            self.send_result(result)

    def send_result(self, message: ResultFromServiceMessage) -> None:
        pickled_message = jsonpickle.encode(message, unpicklable=False)
        queue_name = message.__class__.__name__

        self.qmanager.publish(pickled_message, queue_name)
