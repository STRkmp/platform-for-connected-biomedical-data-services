import cv2
import torch
import numpy as np


def preprocess(ct):
    X = [preprocess_slice(x) for x in ct]
    X = torch.tensor(X)
    X = torch.unsqueeze(X, 1)

    return X

def resize_image_ar(img_ar):

    img_ar = [resize_img(slice) for slice in img_ar]
    img_ar = np.array(img_ar)

    return img_ar

def resize_img(img):
    size = (224, 224)  # (160, 160)
    method = cv2.INTER_AREA

    if img.shape[0] < size[0]:
        method = cv2.INTER_CUBIC

    img_resized = cv2.resize(img, size, interpolation=method)
    return img_resized


def preprocess_slice(img):

    img_resized = resize_img(img)
    norm_img = cv2.normalize(img_resized, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    return norm_img