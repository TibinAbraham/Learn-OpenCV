# Read and Write

import cv2

img = cv2.imread('lena.jpg',1)  #read image in cv2
print(img) # Matrix pixel displayed
cv2.imshow('open_img',img)  # Display image
k = cv2.waitKey(0) # Wait key used to display the image for a time interval

if k == 27:  # if ESC is pressed EXIT
    cv2.destroyAllWindows() # Destroy all the windows created
elif k == ord('s'): # else if 's' save the imaage as new file
    cv2.imwrite('lena_copy.png',img)    # New file created

