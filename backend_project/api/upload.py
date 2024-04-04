from common.utils.minio_utils import upload_to_minio
from .serializers import UploadedFileSerializer
import uuid


def upload_file(file, user_id):
    path = "{}/{}/".format(user_id, str(uuid.uuid4()))
    full_path = path + file.name

    upload_to_minio(full_path, file)

    # Создаем запись о загруженном файле
    serializer = UploadedFileSerializer(data={'full_path': full_path, 'name': file.name})
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return instance