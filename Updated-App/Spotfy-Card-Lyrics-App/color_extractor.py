from sys import flags
from turtle import width
import cv2
import numpy as np

def create_bar(height, width, color):

    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


def return_color_palette(img_path):

    image = cv2.imread(img_path)

    # cv2.imshow('Album Cover', image)
    # cv2.waitKey(0)

    height, width, channel = np.shape(image)
    #print(height, width, channel)

    data = np.reshape(image, (height * width, 3))
    data = np.float32(data)

    num_clusters = 4
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data, num_clusters, None, criteria, 20, flags)
    #print(centers)

    font = cv2.FONT_HERSHEY_SIMPLEX

    bars = []
    rgb_values = []

    for index, row in enumerate(centers):
        bar, rgb = create_bar(200, 200, row)
        bars.append(bar)
        rgb_values.append(rgb)

    img_bar = np.hstack(bars)

    for index, row in enumerate(rgb_values):
        img = cv2.putText(img_bar, f'{index + 1}.RGB: {row}', (5 + 200 * index, 200 - 10), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        # print(f'{index + 1}.RGB{row}')

    # cv2.imshow('Image', image)
    # cv2.imshow('Dominant Colors', img_bar)
    # cv2.waitKey(0)
    
    #Return 4 dominant colors in RGB
    return rgb_values



