import numpy as np
import cv2


class Image_Processing(object):
    def Load_Image(self):
        image = cv2.imread('./Dataset_opencvdl/Q1_Image/Uncle_Roger.jpg')
        cv2.imshow('1', image)

        height = image.shape[0]
        width = image.shape[1]
        print('Height = ', height)
        print('Width = ', width)

    def Color_Separation(self):
        image = cv2.imread('./Dataset_opencvdl/Q1_Image/Flower.jpg')
        cv2.namedWindow('F')
        cv2.imshow('F', image)
        (B, G, R) = cv2.split(image)
        zeros = np.zeros(image.shape[:2], dtype="uint8")
        cv2.namedWindow('B')
        cv2.imshow('B', cv2.merge([B, zeros, zeros]))
        cv2.namedWindow('G')
        cv2.imshow('G', cv2.merge([zeros, G, zeros]))
        cv2.namedWindow('R')
        cv2.imshow('R', cv2.merge([zeros, zeros, R]))

    def Image_Flipping(self):
        image = cv2.imread('./Dataset_opencvdl/Q1_Image/Uncle_Roger.jpg')
        cv2.namedWindow('Original Image')
        cv2.imshow('Original Image', image)
        flip_img = cv2.flip(image, 1)
        cv2.namedWindow('Result')
        cv2.imshow('Result', flip_img)

    def Blending(self):
        org_img = cv2.imread('./Dataset_opencvdl/Q1_Image/Uncle_Roger.jpg')
        flip_img = cv2.flip(org_img, 1)

        def on_trackbar(val):
            alpha = val / 255
            beta = (1.0 - alpha)
            dst = cv2.addWeighted(org_img, alpha, flip_img, beta, 0.0)
            cv2.imshow('BLENDING', dst)

        cv2.namedWindow('BLENDING')
        cv2.createTrackbar('BLEND', 'BLENDING', 0, 255, on_trackbar)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
