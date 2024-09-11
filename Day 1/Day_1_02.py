import cv2

capture = cv2.VideoCapture(0);

'''
while(True):
    ret, frame = capture.read()

    cv2.imshow('window',frame)

    if cv2.waitKey(1) &  0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
'''
import cv2
ret, frame = capture.read()

if ret:  # Check if the frame was captured successfully
    cv2.imshow('window', frame)
    cv2.waitKey(0)  # Wait indefinitely until a key is pressed

# Release the capture and close the window
capture.release()
cv2.destroyAllWindows()



