import cv2, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]                                      # creating empty lists to store data in them
times = []
df = pandas.DataFrame(columns=["Entry", "Exit"])
video_maker = cv2.VideoCapture(0)


while True:
    check, frame = video_maker.read()
    status = 0
    gray_image_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_image_frame = cv2.GaussianBlur(gray_image_frame, (21, 21), 0)      # updating the current frame to have the
                                                                            # GaussianBlur effect

    if first_frame is None:
        first_frame = gray_image_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_image_frame)
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=1)
    (cnts, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:                    # loop for detecting object and raising status == 1
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 256, 0), 3)

    status_list.append(status)                                  # updating the status list!
    status_list = status_list[-2:]                              # updating list to only read the last 2 values

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())                            # to show date_time stamp of object entering and exiting frame
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Gray frame", gray_image_frame)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold frame", threshold_frame)
    cv2.imshow("Colour frame", frame)
    key = cv2.waitKey(1)
    # print(frame)
    # print(delta_frame)

    if key == ord("q"):
        if status == 1:
            times.append(datetime.now())
        break


print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Entry": times[i], "Exit": times[i+1]}, ignore_index=True)     # looping values with (step)=2 in a df


df.to_csv("Time.csv")
video_maker.release()
cv2.destroyAllWindows()
