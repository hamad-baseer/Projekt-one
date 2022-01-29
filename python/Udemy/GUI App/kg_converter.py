from tkinter import *

window=Tk()


def kg_converter():
    grams=float(entry_values.get())*1000
    pounds=float(entry_values.get())*2.20462
    ounces=float(entry_values.get())*35.274
    text.delete("1.0", END)
    text.insert(END, grams)
    text1.delete("1.0", END)
    text1.insert(END, pounds)
    text2.delete("1.0", END)
    text2.insert(END, ounces)


label=Label(window, text="Kilogram:")
label.grid(row=0, column=0)
button=Button(window, text="Convert", command=kg_converter)
button.grid(row=0, column=3)
entry_values=StringVar()
entry=Entry(window, textvariable=entry_values, width=25)
entry.grid(row=0, column=2)
text=Text(window, height=1, width=25)
text.grid(row=1, column=0)
text1=Text(window, height=1, width=25)
text1.grid(row=1, column=1)
text2=Text(window, height=1, width=25)
text2.grid(row=1, column=2)


window.mainloop()