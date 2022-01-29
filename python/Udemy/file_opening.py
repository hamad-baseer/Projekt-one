import time
import os

while True:
    if os.path.exists("Course materials etc/fruits.txt"):
        with open("Course materials etc/fruits.txt") as file:
            print(file.read())
    else:
        print("File does not Exist!")
    time.sleep(10)


import time

while True:
    with open("Course materials etc/fruits.txt") as file:
        data2 = file.read()
        print(data2)
        time.sleep(10)


file_opener = open("Course materials etc/fruits.txt")
data = file_opener.read()
file_opener.close()

with open("Course materials etc/fruits.txt") as my_file:
    data1 = my_file.read()


with open("bear.txt", "r") as my_file1:
    content = my_file1.read()

with open("first.txt", "w") as my_file2:
    my_file2.write(content[:90])


