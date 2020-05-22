import cv2
import numpy as np
from Q2 import greyscale


def thresholding(img, threshold = 128):
    g_img = np.where(img<threshold, 0, 255)

    return g_img


if __name__ == "__main__":
    img = cv2.imread("../imori.jpg")
    g_img = greyscale(img)
    img = thresholding(g_img)
    cv2.imwrite("answer_3.jpg", img)
