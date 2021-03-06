import cv2
# Create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier(
    ".\Project\haarcascade_frontalface_default.xml")

# Create the camera object
cap = cv2.VideoCapture(0)

# Callback function
def nothing(x):
    pass


cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Neighbors", "image", 5, 20, nothing)

# Read the image and process it
while(cap.isOpened()):
    ret, img = cap.read()
    if ret:
        # Reading the image as gray scale image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Search the co-ordinates of the image
        # Decreased the shape value by 5%, until the face is found. Smaller this value, the greater is the accuracy.
        neighbors = cv2.getTrackbarPos('Neighbors', 'image')
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                              minNeighbors=neighbors, minSize=(1, 1))
        # print(type(faces))
        # print(faces)
        # Draw the rectangle box around the detected faces
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            print("No faces detected in the image!")

        if (cv2.waitKey(1) & 0xFF) in [ord('q'), 27]:
            break
        cv2.imshow('image', img)

cap.release()
cv2.destroyAllWindows()
