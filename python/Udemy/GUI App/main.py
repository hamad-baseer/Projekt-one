from tkinter import *


window=Tk()


def km_to_miles():
    miles=float(entry_value.get())/1.6
    text.delete("1.0", END)
    text.insert(END, miles)


label=Label(window, text="Convert kms to miles:")
label.grid(row=0, column=0)
entry_value=StringVar()
entry=Entry(window, textvariable=entry_value)
entry.grid(row=0, column=1)
button=Button(window, text="Convert", command=km_to_miles)
button.grid(row=0, column=2)
text=Text(window, height=1, width=25)
text.grid(row=1, column=0)


def miles_to_km():
    kms=float(entry_value1.get())*1.6
    text1.delete("1.0", END)
    text1.insert(END, kms)


label1=Label(window, text="Convert miles to kms:")
label1.grid(row=2, column=0)
entry_value1=StringVar()
entry1=Entry(window, textvariable=entry_value1)
entry1.grid(row=2, column=1)
button1=Button(window, text="Convert", command=miles_to_km)
button1.grid(row=2, column=2)
text1=Text(window, height=1, width=25)
text1.grid(row=3, column=0)


window.mainloop()
