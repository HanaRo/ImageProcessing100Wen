import cv2
import numpy as np


def greyscale(img):
    f_img = img.copy().astype(np.float32)

    b = f_img[:, :, 0].copy()
    g = f_img[:, :, 1].copy()
    r = f_img[:, :, 2].copy()

    y = 0.2126*r + 0.7152*g + 0.0722*b
    y = y.astype(np.uint8)

    return y


if __name__ == "__main__":
    img = cv2.imread("../imori.jpg")
    img = greyscale(img)
    cv2.imwrite("answer_2.jpg", img)

    # Show image
    # cv2.imshow("", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
