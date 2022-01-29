import cv2, time

video_maker = cv2.VideoCapture(0)

frames = 0
while True:
    check, frame = video_maker.read()
    print(check)
    print(frame)
    # gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Live Video", frame)
    frames = frames+1
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

print("frames: ", frames)
video_maker.release()
cv2.destroyAllWindows()
