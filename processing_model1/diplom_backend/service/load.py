import SimpleITK as sitk

import os
import uuid
import zipfile

def get_path_to_file(file, file_info):
    path, is_dir = handle_uploaded_file(file, file_info)
    return path, is_dir


def handle_uploaded_file(f, file_info):
    is_dir = False
    uuid_str = str(uuid.uuid1())
    filename = os.path.basename(file_info.object_name)
    temp_name = uuid_str + "-" + filename
    path = os.path.join(os.getcwd(), 'temp', temp_name)
    print(f'путь к файлу временному - {path}')
    with open(path, 'wb+') as destination:
        for chunk in f.stream(1024 * 1024):
            destination.write(chunk)

    if filename.endswith('.zip'):
        temp_dir = os.path.join('temp', temp_name.replace(".zip", ""))
        print('temp_dir = ', temp_dir)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(os.path.join('temp', temp_dir))
        is_dir = True
        os.remove(path)
        path = temp_dir

    return path, is_dir


def load_image(filename):
    image = sitk.ReadImage(filename)
    ct_scan = sitk.GetArrayFromImage(image)

    return image, ct_scan