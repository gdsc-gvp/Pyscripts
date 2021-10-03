import urllib.request
import cv2
import numpy as np


def grayscale_filter(image):

    new_image_shape = (image.shape[0], image.shape[1])
    grayscaled_image = np.zeros(new_image_shape)

    for i in range(new_image_shape[0]):
        for j in range(new_image_shape[1]):
            r, g, b = image[i][j]

            # 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
            grayscaled_image[i][j] = (0.299 *
                                      (r/255) + 0.587 * (g/255) + 0.114 * (b/255))

    return grayscaled_image


# Path for the image
image_path = './cat.png'
img = None

try:
    img = cv2.imread(image_path)
except Exception:
    urllib.request.urlretrieve(
        'https://images.unsplash.com/photo-1615789591457-74a63395c990?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YmFieSUyMGNhdHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80',
        "cat.png")
    img = cv2.imread('cat.png')

# convert to grayscale
grayscaled_image = grayscale_filter(img)
cv2.imwrite('grayscaled_image.png', 255*grayscaled_image)
cv2.imshow('original image', img)
cv2.imshow('image with grayscale filter', grayscaled_image)
cv2.waitKey(0)
