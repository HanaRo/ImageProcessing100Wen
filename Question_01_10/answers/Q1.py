import cv2


def swap_bgr(img):
    red = img[:, :, 2].copy()
    green = img[:, :, 1].copy()
    blue = img[:, :, 0].copy()

    img[:, :, 0] = red
    img[:, :, 1] = green
    img[:, :, 2] = blue

    return img


if __name__ == "__main__":
    img = cv2.imread("../imori.jpg")
    img = swap_bgr(img)
    cv2.imwrite("answer_1.jpg", img)

    # Show image
    # cv2.imshow("", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
