import cv2
import glob

images = glob.glob("Course materials etc/*.jpg")


for image in images:
    img = cv2.imread(image, 1)
    resized_img = cv2.resize(img, (int(img.shape[0]/2), int(img.shape[1]/2)))
    cv2.imshow("sample", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, resized_img)

