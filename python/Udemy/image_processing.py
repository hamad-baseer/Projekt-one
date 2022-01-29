import cv2

image=cv2.imread("Course materials etc/galaxy.jpg", 1)

print(image)
print(image.shape)
print(image.ndim)


resized_image = cv2.resize(image, (int(image.shape[0]/2), int(image.shape[1]/2)))
cv2.imshow("galaxy", resized_image)
cv2.imwrite("resized_galaxy.jpg", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
