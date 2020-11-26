---
title: Python-OpenCV 練習
tags: OpenCV, Python
---
## Description
This is a practice project that using Python with OpenCV.

## Requirements
* Python==3.7.0
* opencv-contrib-python==3.4.2.17
* matplotlib==3.1.1
* numpy==1.18.5
* PyQt5==5.15.1
* pyqt5-tools==5.15.1

---

## Show the results
### 1. Image Processing
#### 1) Load Image File 

![](https://i.imgur.com/cuhLXBW.jpg)

#### 2) Color Separation 
Extract 3 channels of the image BGR to 3 separated channels.

![](https://i.imgur.com/wwNBhPE.jpg)

![](https://i.imgur.com/WUMg5fB.jpg)

![](https://i.imgur.com/DAgVkm2.jpg)

![](https://i.imgur.com/k1ldK6p.jpg)

#### 3) Image Flipping 
Flip the image 

![](https://i.imgur.com/sUdvl0n.jpg)

![](https://i.imgur.com/FxGxlmB.jpg)

#### 4) Blending 
Combine two images and ese Trackbar to change the weights and show the result.

![](https://i.imgur.com/54Xz9zr.jpg)

![](https://i.imgur.com/ZuN0SW6.jpg)

![](https://i.imgur.com/QLQu7DU.jpg)

### 2. Image Smoothing
Original image:

![](https://i.imgur.com/yQa4feC.jpg)

#### 1) Median filter 
Apply 7x7 median filter.

![](https://i.imgur.com/eCqYI9M.jpg)

#### 2) Gaussian blur 
Apply 3x3 Gaussian blur.

![](https://i.imgur.com/7iXFkPr.jpg)

#### 3) Bilateral filter 
Apply 9x9 Bilateral filter with 90 sigmaColor and 90 sigmaSpace.

![](https://i.imgur.com/97s0Hr2.jpg)

### 3. Edge Detection
Original image:

![](https://i.imgur.com/har3im0.jpg)

#### 1) Gaussian Blur(without OpenCV)

![](https://i.imgur.com/TEuqbvK.jpg)

#### 2) Sobel X

![](https://i.imgur.com/7ZsrQYm.jpg)

#### 3) Sobel Y

![](https://i.imgur.com/ubQF8jK.jpg)

#### 4) Magnitude
Use the results of Sobel X and Sobel Y to calculate the magnitude. 

![](https://i.imgur.com/2AY7wYO.jpg)


### 4. Transforms
With Rotation, Scaling, Translation with (x, y) as following parameters: 

![](https://i.imgur.com/LYUaObq.jpg)

Original image:
![](https://i.imgur.com/p6fZ1kZ.png)

After transform:
![](https://i.imgur.com/oDVAyQN.jpg)

