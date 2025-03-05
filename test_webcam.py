import cv2

cap = cv2.VideoCapture(0) #open the webcam

while True:
    ret, frame = cap.read() # Capture frame-by-frame
    if not ret:
        break #exit the loop if there is no frame

    cv2.imshow("Webcam Test", frame) # Display the resulting frame

    #press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release() # When everything done, release the capture
    cv2.destroyAllWindows() # Destroy the window
    