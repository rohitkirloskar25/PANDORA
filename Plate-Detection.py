import cv2
import numpy
import matplotlib.pyplot as plt
%matplotlib inline


# IMAGE SCALING
def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img)


# ALGORITHM TO PLATE DETECTION
plate_cascade = cv2.CascadeClassifier('path to your haarcascade algo')


# PLATE DETECTION FUNCTION
def detect_plate(img):  
  
    plate_img = img.copy()
    plate_copy = plate.copy()
  
    plate_rects = plate_cascade.detectMultiScale(plate_img) 
    
    for (x,y,w,h) in plate_rects: 
        cv2.rectangle(plate_copy, (x,y), (x+w,y+h), (0,255,0), 15) 
        
        
    return plate_copy


# IMPORT AND PROCESS IMAGE
plate = cv2.imread('path to your image')
plate = cv2.cvtColor(plate, cv2.COLOR_BGR2RGB) 
display_img(plate)


# BLUR AND DISPLAY THE IMAGE
blurred = cv2.blur(plate, (40,40)) 
display_img(blurred)


# DETECT THE PLATE AND DISPLAY THE GREEN DETECTION
result = detect_plate(blurred)
display_img(result)