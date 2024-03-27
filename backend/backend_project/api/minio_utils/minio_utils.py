import io, os
from minio import Minio
from minio.error import S3Error

minio_client = Minio(
    'minio:9000',
    access_key=os.environ.get('MINIO_ACCESS_KEY'),  # Обновлено здесь
    secret_key=os.environ.get('MINIO_SECRET_KEY'),  # Обновлено здесь
    secure=False
)


def upload_to_minio(bucket_name, file_name, file_data, content_type):
    try:
        minio_client.put_object(
            bucket_name,
            file_name,
            io.BytesIO(file_data),
            len(file_data),
            content_type=content_type
        )
        return {'status': 'success', 'message': 'File uploaded to MinIO successfully'}
    except S3Error as err:
        return {'status': 'error', 'message': f'Error uploading file to MinIO: {err}'}