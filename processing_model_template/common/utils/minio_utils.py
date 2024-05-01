import os
from io import BytesIO
from minio import Minio

minio_client = Minio(
    endpoint=os.environ.get('MINIO_ENDPOINT', 'localhost:9000'),
    access_key=os.environ.get('MINIO_ACCESS_KEY', 'djangoAppUser'),  # Обновлено здесь
    secret_key=os.environ.get('MINIO_SECRET_KEY', 'djangoAppUserSecretKey'),  # Обновлено здесь
    secure=False
)

bucket = os.environ.get('MINIO_BUCKET', 'platform')


def upload_to_minio(file_name, file):
    try:
        file_stream = BytesIO(file.read())
        file_size = file_stream.getbuffer().nbytes

        minio_client.put_object(
            bucket,
            file_name,
            file_stream,
            file_size
        )
    except Exception as err:
        print("Ошибка при загрузке файла. {}".format(err))
        raise err


def get_object_from_minio(file_name):
    try:
        return minio_client.get_object(bucket, file_name)
    except Exception as err:
        print("Ошибка при чтении файла. {}".format(err))
        raise err


def replace_path_file(file_path, new_file_name):
    # Находим позицию последнего символа '/'
    last_slash_index = file_path.rfind('/')

    if last_slash_index != -1:
        # Выделяем путь к файлу и его имя
        path = file_path[:last_slash_index + 1]

        # Формируем новый путь с новым именем файла
        new_file_path = path + new_file_name
        return new_file_path
    else:
        # Если нет символа '/', то возвращаем исходный путь
        return new_file_name