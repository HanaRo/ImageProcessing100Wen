import cv2
import numpy as np


def greyscale(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    y = 0.2126*r + 0.7152*g + 0.0722*b

    return y


if __name__ == "__main__":
    img = cv2.imread("../imori.jpg")
    f_img = img.copy().astype(np.float32)
    img = greyscale(f_img)
    cv2.imwrite("answer_2.jpg", img.astype(np.uint8))

    # Show image
    # cv2.imshow("", img.astype(np.uint8))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
