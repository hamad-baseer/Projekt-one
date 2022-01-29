from tkinter import *
from database import Database


database=Database("books.db")
selected_tuple = ()


class AppInterface(object):

    def __init__(self, window):
        self.window=window
        self.window.wm_title("Digital Bookstore")

        # labels
        label=Label(window,text="Title")
        label1=Label(window,text="Author")
        label2=Label(window,text="Year")
        label3=Label(window,text="ISBN")
        label.grid(row=0,column=0)
        label1.grid(row=0, column=2)
        label2.grid(row=1,column=0)
        label3.grid(row=1,column=2)

        # Entry box
        self.title_string=StringVar()
        self.entry_box=Entry(window, textvariable=self.title_string)
        self.author_string=StringVar()
        self.entry_box1=Entry(window, textvariable=self.author_string)
        self.year_string=StringVar()
        self.entry_box2=Entry(window, textvariable=self.year_string)
        self.isbn_string=StringVar()
        self.entry_box3=Entry(window, textvariable=self.isbn_string)
        self.entry_box.grid(row=0,column=1)
        self.entry_box1.grid(row=0,column=3)
        self.entry_box2.grid(row=1,column=1)
        self.entry_box3.grid(row=1,column=3)

        # Textbox for showing info
        self.text_box=Listbox(window, height=15, width=18)
        self.text_box.grid(row=3,column=0,rowspan=10, columnspan=2)

        # Buttons for all
        button=Button(window, text="View all", width=10, command=self.view_button)
        button1=Button(window, text="Search Entry", width=10, command=self.search_button)
        button2=Button(window, text="Add Entry", width=10, command=self.entry_button)
        button3=Button(window, text="Update", width=10, command=self.update_button)
        button4=Button(window, text="Delete", width=10, command=self.delete_button)
        button5=Button(window, text="Close", width=10, command=window.destroy)
        button6=Button(window, text="Clear all", width=10, command=self.clear_entries)
        button.grid(row=3, column=3)
        button1.grid(row=4,column=3)
        button2.grid(row=5,column=3)
        button3.grid(row=6,column=3)
        button4.grid(row=7, column=3)
        button5.grid(row=8,column=3)
        button6.grid(row=9,column=3)

        scroll_bar=Scrollbar(window)
        scroll_bar.grid(row=3,column=2,rowspan=10)
        self.text_box.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.configure(command=self.text_box.yview())

        self.text_box.bind("<<ListboxSelect>>", self.show_selected_data)

    def show_selected_data(self, event):
        try:
            global selected_tuple
            index=self.text_box.curselection()[0]
            selected_tuple=self.text_box.get(index)
            self.entry_box.delete(0, END)
            self.entry_box.insert(END, selected_tuple[1])
            self.entry_box1.delete(0, END)
            self.entry_box1.insert(END, selected_tuple[2])
            self.entry_box2.delete(0, END)
            self.entry_box2.insert(END, selected_tuple[3])
            self.entry_box3.delete(0, END)
            self.entry_box3.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def view_button(self):
        self.text_box.delete(0, END)
        for row in database.view():
            self.text_box.insert(END, row)

    def search_button(self):
        self.text_box.delete(0, END)
        for row in database.search(self.title_string.get(), self.author_string.get(), self.year_string.get(), self.isbn_string.get()):
            self.text_box.insert(END, row)

    def entry_button(self):
        database.insert(self.title_string.get(), self.author_string.get(), self.year_string.get(), self.isbn_string.get())
        self.text_box.delete(0, END)
        self.text_box.insert(END, (self.title_string.get(), self.author_string.get(), self.year_string.get(), self.isbn_string.get()))
        self.clear_entries()
        self.view_button()

    def clear_entries(self):
        self.entry_box.delete(0, END)
        self.entry_box1.delete(0, END)
        self.entry_box2.delete(0, END)
        self.entry_box3.delete(0, END)

    def delete_button(self):
        database.delete(selected_tuple[0])
        self.clear_entries()
        self.view_button()

    def update_button(self):
        database.update(selected_tuple[0], self.title_string.get(), self.author_string.get(), self.year_string.get(), self.isbn_string.get())
        self.view_button()


window=Tk()
AppInterface(window)
window.mainloop()
