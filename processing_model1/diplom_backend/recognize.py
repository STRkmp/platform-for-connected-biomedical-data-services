import os
from multiprocessing.pool import ThreadPool
from diplom_backend.service.report import make_report
from diplom_backend.service.recognize import run_model
from diplom_backend.service.preprocess import preprocess, resize_image_ar
from diplom_backend.service.load import get_path_to_file, load_image
from diplom_backend.service.segment_lung import get_volume_lesion, segmentation_lung


def start_recognize(file, file_info):
    path, is_dir = get_path_to_file(file, file_info)

    if is_dir:
        files_in_dir = os.listdir(path)
        name_file = [x for x in files_in_dir if x.split('.')[-1] == 'mhd'][0]
        path = os.path.join(path, name_file)

    ct, ct_matrix = load_image(path)

    mask_lung = segmentation_lung(ct)

    ct_preprocess = preprocess(ct_matrix)
    mask_lesion = run_model(ct_preprocess)

    mask_lung = resize_image_ar(mask_lung)

    volume_lesion = get_volume_lesion(mask_lung, mask_lesion)

    data_for_report = {
        'volume_lesion': str(volume_lesion['lung']),
        'volume_lesion_left': str(volume_lesion['left']),
        'volume_lesion_right': str(volume_lesion['right']),
    }

    report = make_report(ct_preprocess, mask_lesion, data_for_report)

    return report.convert_to_pdf()
