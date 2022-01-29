import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("Course materials etc/photo.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)


for x_axis, y_axis, width, height in faces:
    image = cv2.rectangle(image, (x_axis, y_axis), (x_axis+width, y_axis+height), (0, 256, 0), 3)
    # updating the image here!. Don't need to create another variable as it won't make sense!

print(faces)
resized_image=cv2.resize(image, (int(image.shape[0]/2), int(image.shape[1]/2)))
cv2.imshow("gray", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
