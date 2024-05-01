import os
from io import BytesIO
from minio import Minio
from datetime import timedelta

minio_client = Minio(
    endpoint=os.environ.get('MINIO_ENDPOINT', 'minio:9000'),
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


def get_presigned_download_url(full_path):
    return minio_client.presigned_get_object(bucket, full_path, expires=timedelta(hours=2))

def get_object_from_minio(file_name):
    try:
        return minio_client.get_object(bucket, file_name)
    except Exception as err:
        print("Ошибка при чтении файла. {}".format(err))
        raise err
