import cv2


class Image_Smoothing(object):
    def Median_Filter(self):
        image = cv2.imread('./Dataset_opencvdl/Q2_Image/Cat.png')
        # cv2.namedWindow('original')
        # cv2.imshow('original', image)
        median = cv2.medianBlur(image, 7)
        cv2.namedWindow('Median')
        cv2.imshow('Median', median)

    def Gaussian_Blur(self):
        image = cv2.imread('./Dataset_opencvdl/Q2_Image/Cat.png')
        # cv2.namedWindow('original')
        # cv2.imshow('original', image)
        guassian = cv2.GaussianBlur(image, (3, 3), 0)
        cv2.namedWindow('Gaussian')
        cv2.imshow('Gaussian', guassian)

    def Bilateral_Filter(self):
        image = cv2.imread('./Dataset_opencvdl/Q2_Image/Cat.png')
        # cv2.namedWindow('original')
        # cv2.imshow('original', image)
        bilateral = cv2.bilateralFilter(image, 9, 90, 90)
        cv2.namedWindow('Bilateral')
        cv2.imshow('Bilateral', bilateral)
