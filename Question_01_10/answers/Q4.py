import cv2
import numpy as np
from Q2 import greyscale
from Q3 import thresholding


def otsu_method(img):
    """
    Search all pixels in the image: inefficient method!
    :param img: greyscale image
    :return: threshold using otsu method
    """
    sorted_array = np.sort(img.flatten())

    sb2 = []
    for i in range(1, len(sorted_array)):
        w0 = i / len(sorted_array)
        w1 = 1 - w0
        m0 = np.mean(sorted_array[:i])
        m1 = np.mean(sorted_array[i:])
        sb2.append(w0 * w1 * np.square(m0 - m1))
    sb2 = np.array(sb2)
    th = sorted_array[sb2.argmax()]
    print('th = ', th)

    return thresholding(img, th)


if __name__ == "__main__":
    img = cv2.imread("../imori.jpg")
    img = greyscale(img)
    img = otsu_method(img)
    cv2.imwrite("answer_4.jpg", img)