from tkinter import *


class MainWindow(Frame):
    """ Layout for the Main Window """

    def __init__(self, parent, contoller):
        """ Initialize Main Application """
        Frame.__init__(self, parent)
        parent.title('Video Downloader')

        # add a menu here
        main_menu = Menu(parent)
        parent.config(menu=main_menu)
        file_menu = Menu(main_menu)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="No Command Yet", command="")
        file_menu.add_command(label="No Command Yet", command="")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # define frames here
        left_frame = Frame(parent)
        left_frame.pack(side=LEFT)
        right_frame = Frame(parent)
        right_frame.pack(side=RIGHT)
        # define labels here
        enter_label = Label(left_frame, text="Enter Link: ")
        enter_label.pack(side=LEFT)
        # define entry box here
        self.entry_link = Entry(left_frame, width="40")
        self.entry_link.pack(side=LEFT)

        # (optional) we can add a scrollbar for listbox here
        self.listbox = Listbox(right_frame, height="30", width="50")
        self.listbox.pack()
        # define buttons here
        download_button = Button(left_frame, text="Download", fg="white", bg="black")
        download_button.bind("<Button-1>", contoller.download_callback)
        download_button.pack(side=BOTTOM)

    # methods are defined here (outside of __init__() )
    def insert_to_listbox(self, titles):
        """"""
        self.listbox.delete(0, END)
        for title in titles:
            self.listbox.insert(END, title)

    def get_link(self):
        """ returns the URL entered in the entry box"""
        return self.entry_link.get()
