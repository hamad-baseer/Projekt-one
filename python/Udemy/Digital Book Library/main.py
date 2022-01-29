from tkinter import *
import database

selected_tuple = ()


def show_selected_data(event):
    try:
        global selected_tuple
        index=text_box.curselection()[0]
        selected_tuple=text_box.get(index)
        entry_box.delete(0, END)
        entry_box.insert(END, selected_tuple[1])
        entry_box1.delete(0, END)
        entry_box1.insert(END, selected_tuple[2])
        entry_box2.delete(0, END)
        entry_box2.insert(END, selected_tuple[3])
        entry_box3.delete(0, END)
        entry_box3.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_button():
    text_box.delete(0, END)
    for row in database.view():
        text_box.insert(END, row)


def search_button():
    text_box.delete(0, END)
    for row in database.search(title_string.get(), author_string.get(), year_string.get(), isbn_string.get()):
        text_box.insert(END, row)


def entry_button():
    database.insert(title_string.get(), author_string.get(), year_string.get(), isbn_string.get())
    text_box.delete(0, END)
    text_box.insert(END, (title_string.get(), author_string.get(), year_string.get(), isbn_string.get()))
    clear_entries()
    view_button()


def clear_entries():
    entry_box.delete(0, END)
    entry_box1.delete(0, END)
    entry_box2.delete(0, END)
    entry_box3.delete(0, END)


def delete_button():
    database.delete(selected_tuple[0])
    clear_entries()
    view_button()


def update_button():
    database.update(selected_tuple[0],title_string.get(), author_string.get(), year_string.get(), isbn_string.get())
    view_button()


window=Tk()
window.wm_title("Digital Bookstore")


label=Label(window,text="Title")
label1=Label(window,text="Author")
label2=Label(window,text="Year")
label3=Label(window,text="ISBN")
label.grid(row=0,column=0)
label1.grid(row=0, column=2)
label2.grid(row=1,column=0)
label3.grid(row=1,column=2)

title_string=StringVar()
entry_box=Entry(window, textvariable=title_string)
author_string=StringVar()
entry_box1=Entry(window, textvariable=author_string)
year_string=StringVar()
entry_box2=Entry(window, textvariable=year_string)
isbn_string=StringVar()
entry_box3=Entry(window, textvariable=isbn_string)
entry_box.grid(row=0,column=1)
entry_box1.grid(row=0,column=3)
entry_box2.grid(row=1,column=1)
entry_box3.grid(row=1,column=3)

text_box=Listbox(window, height=15, width=18)
text_box.grid(row=3,column=0,rowspan=10, columnspan=2)

button=Button(window, text="View all", width=10, command=view_button)
button1=Button(window, text="Search Entry", width=10, command=search_button)
button2=Button(window, text="Add Entry", width=10, command=entry_button)
button3=Button(window, text="Update", width=10, command=update_button)
button4=Button(window, text="Delete", width=10, command=delete_button)
button5=Button(window, text="Close", width=10, command=window.destroy)
button.grid(row=3, column=3)
button1.grid(row=4,column=3)
button2.grid(row=5,column=3)
button3.grid(row=6,column=3)
button4.grid(row=7, column=3)
button5.grid(row=8,column=3)

scroll_bar=Scrollbar(window)
scroll_bar.grid(row=3,column=2,rowspan=10)
text_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=text_box.yview())

text_box.bind("<<ListboxSelect>>", show_selected_data)

window.mainloop()
