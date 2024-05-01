import numpy as np
from lungmask import mask as segmentator
import cv2
from diplom_backend.service.preprocess import  resize_image_ar

def get_volume_lesion(mask_lung, mask_lesion):

    # mask_lung = [cv2.resize(slice, (224, 224)) for slice in mask_lung]
    # mask_lung = np.array(mask_lung)
    mask_lung = resize_image_ar(mask_lung)

    print(mask_lung.shape, mask_lesion.shape)
    unique_value_lung = np.unique(mask_lung, return_counts=True)[1]
    count_pixel_lung = unique_value_lung[1] + unique_value_lung[2]
    print('count_pixel_lung = ', count_pixel_lung, 'unique_value_lung = ', unique_value_lung)

    uniq_val_mask = np.unique(mask_lesion, return_counts=True)[1]
    count_pixel_lesion = uniq_val_mask[1]
    print('count_pixel_lesion = ', count_pixel_lesion, 'uniq_val_mask = ', uniq_val_mask)


    cols_by_2 = int(mask_lesion.shape[2] / 2)
    count_pixel_left_lesion = np.unique(mask_lesion[:, :, 0:cols_by_2], return_counts=True)[1][1]
    count_pixel_right_lesion = np.unique(mask_lesion[:, :, cols_by_2:], return_counts=True)[1][1]
    print('count_pixel_left_lesion =', count_pixel_left_lesion, 'count_pixel_right_lesion = ', count_pixel_right_lesion)


    # volume = (count_pixel_lesion / count_pixel_lung) * 100
    # print('volume = ', volume)


    volume_left = (count_pixel_left_lesion / unique_value_lung[1]) * 100
    volume_right = (count_pixel_right_lesion / unique_value_lung[2]) * 100
    volume = volume_left + volume_right

    volume = volume_left + volume_right


    return {
        'lung': np.round(volume, 5),
        'left': np.round(volume_left, 5),
        'right':  np.round(volume_right, 5)
    }

def segmentation_lung(ct):
    segmentation = segmentator.apply(ct)
    return segmentation
