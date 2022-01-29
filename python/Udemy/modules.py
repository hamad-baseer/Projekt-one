import time
import os
import pandas

while True:
    if os.path.exists("Course materials etc/temps_today.csv"):
        dataframe = pandas.read_csv("Course materials etc/temps_today.csv")
        print(dataframe.mean())
    else:
        print("File does not Exist!")
    time.sleep(10)
