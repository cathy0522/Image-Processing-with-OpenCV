import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import signal
from scipy.ndimage import filters


class Edge_Detection(object):
    def Gaussian_nocv(self):
        image = cv2.imread('./Dataset_opencvdl/Q3_Image/Chihiro.jpg')
        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # 3*3 Gaussian Filter
        x, y = np.mgrid[-1:2, -1:2]
        gaussian_kernel = np.exp(-(x ** 2 + y ** 2))
        # Normalization
        gaussian_kernel = gaussian_kernel / gaussian_kernel.sum()

        grad = signal.convolve2d(gray_img, gaussian_kernel, boundary='symm', mode='same')  # convolution

        plt.imshow(grad, cmap=plt.get_cmap('gray'))
        plt.axis('off')
        plt.show()

    def Sobel_X(self):
        image = cv2.imread('./Dataset_opencvdl/Q3_Image/Chihiro.jpg')
        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray_img = np.array(gray_img)

        img_X = np.zeros(gray_img.shape)
        # Filter
        filters.sobel(gray_img, 1, img_X)
        # Normalization
        img_X *= (img_X - np.min(img_X)) / (np.max(img_X) - np.min(img_X))

        plt.imshow(img_X, cmap='gray')
        plt.axis('off')
        plt.show()

    def Sobel_Y(self):
        image = cv2.imread('./Dataset_opencvdl/Q3_Image/Chihiro.jpg')
        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray_img = np.array(gray_img)

        img_Y = np.zeros(gray_img.shape)
        # Filter
        filters.sobel(gray_img, 0, img_Y)
        # Normalization
        img_Y *= (img_Y - np.min(img_Y)) / (np.max(img_Y) - np.min(img_Y))

        plt.imshow(img_Y, cmap='gray')
        plt.axis('off')
        plt.show()

    def Magnitude(self):
        image = cv2.imread('./Dataset_opencvdl/Q3_Image/Chihiro.jpg')
        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray_img = np.array(gray_img)

        img_X = np.zeros(gray_img.shape)
        filters.sobel(gray_img, 1, img_X)
        img_Y = np.zeros(gray_img.shape)
        filters.sobel(gray_img, 0, img_Y)

        # Filter
        mag = np.hypot(img_X, img_Y)
        # Normalization
        mag *= 255.0 / np.max(mag)

        plt.imshow(mag, cmap='gray')
        plt.axis('off')
        plt.show()
