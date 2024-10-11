import cv2  
import matplotlib.pyplot as plt  
import numpy as np  

image1 = cv2.imread('image.png')  

if image1 is None:  
    print("Error: Image not found.")  
else:  
    training_image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)  

    training_gray = cv2.cvtColor(training_image, cv2.COLOR_RGB2GRAY)  

    test_image = cv2.pyrDown(training_image)  
    test_image = cv2.pyrDown(test_image)  
    num_rows, num_cols = test_image.shape[:2]  

    rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), 30, 1)  
    test_image = cv2.warpAffine(test_image, rotation_matrix, (num_cols, num_rows))  

    test_gray = cv2.cvtColor(test_image, cv2.COLOR_RGB2GRAY)  

    #fig, plots = plt.subplots(1, 2, figsize=(20, 10))  
    #plots[0].set_title("Training Image")  
    #plots[0].
    cv2.imshow("ori",training_image)  
    #plots[0].axis('off')  # Hide axes for better visualization  

    #plots[1].set_title("Testing Image")  
    #plots[1].
    cv2.imshow("res",test_image)  
    #plots[1].axis('off')  # Hide axes for better visualization  
    #plt.show()  

    sift = cv2.SIFT_create()  

    keypoints_train, descriptors_train = sift.detectAndCompute(training_gray, None)  
    keypoints_test, descriptors_test = sift.detectAndCompute(test_gray, None)  

    training_image_with_keypoints = cv2.drawKeypoints(training_image, keypoints_train, None)  
    test_image_with_keypoints = cv2.drawKeypoints(test_image, keypoints_test, None)  

    #fig, plots = plt.subplots(1, 2, figsize=(20, 10))  
    #plots[0].set_title("Training Image with Keypoints")  
    #plots[0].
    cv2.imshow("training_image_with_keypoints",training_image_with_keypoints)  
    #plots[0].axis('off')  

    #plots[1].set_title("Testing Image with Keypoints")  
    #plots[1].
    cv2.imshow("test_image_with_keypoints",test_image_with_keypoints)  
    #plots[1].axis('off')  

    #plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()