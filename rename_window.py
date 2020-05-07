from tkinter import *


class RenameWindow(Frame):
    """ Layout for the Main Window """

    def __init__(self, parent, contoller, title):
        """ Initialize Main Application """
        Frame.__init__(self, parent)
        parent.title('Rename')

        # define frames
        left_frame = Frame(parent, bg='gray37')
        left_frame.pack(side=TOP)

        right_frame = Frame(parent)
        right_frame.pack()

        # define label that has the title you want to rename
        title_label = Label(left_frame, text=title, bg='gray37', fg="white")
        title_label.grid(row=0, pady=10)

        # define entry box
        self.entry_name = Entry(right_frame, width="40")
        self.entry_name.grid(row=1, column=0 ,padx=5 , pady=5)

        # define save button
        save_button = Button(right_frame, text="Save", fg="white", bg="RoyalBlue1")
        save_button.bind("<Button-1>", contoller.update_title)
        save_button.grid(row=1,column=1, padx=5, pady=5)

    def get_form_data(self):
        """ Return a dictionary of form field values with updated title """
        return {
            "title": self.entry_name.get()
        }

    def clear_form_fields(self):
        """ Clear the name entry box """
        self.entry_name.delete(0, END)
