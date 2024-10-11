import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img = cv2.imread("image.png") 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color display 
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert to grayscale for processing 
plt.figure(figsize=(20, 20)) 
plt.subplot(221) 
plt.title('Original') 
plt.imshow(img) 
plt.axis('off')  # Hide axes for better visualization 
img_hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256]) 
plt.subplot(222) 
plt.title('Grayscale Histogram') 
plt.plot(img_hist) 
plt.subplot(223) 
plt.hist(img_gray.ravel(), 256, [0, 256]) 
plt.title('Histogram using ravel()') 
equalized_img = cv2.equalizeHist(img_gray) 
plt.subplot(224) 
plt.title('Equalized Image') 
plt.imshow(equalized_img, cmap='gray') 
plt.axis('off') 
plt.show() 

 