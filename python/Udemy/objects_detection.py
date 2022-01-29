import cv2

first_frame = None
video_maker = cv2.VideoCapture(0)


while True:
    check, frame = video_maker.read()
    gray_image_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_image_frame = cv2.GaussianBlur(gray_image_frame, (21, 21), 0)      # updating the current frame to have the
                                                                            # GaussianBlur effect

    if first_frame is None:
        first_frame = gray_image_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_image_frame)
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=1)
    (cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 256, 0), 3)

    cv2.imshow("Gray frame", gray_image_frame)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold frame", threshold_frame)
    cv2.imshow("Colour frame", frame)
    key = cv2.waitKey(1)
    print(frame)
    print(delta_frame)

    if key == ord("q"):
        break

video_maker.release()
cv2.destroyAllWindows()
