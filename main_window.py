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
        win = Frame(parent)
        win.pack(side="top", fill="both", expand=True)
        win.grid_columnconfigure(2, weight=1)
        win.grid_rowconfigure(2, weight=1)
       # left_frame = Frame(parent)
       # left_frame.pack(side=LEFT)
        #right_frame = Frame(parent)
        #right_frame.pack(side=RIGHT)
        # define labels
        entrystuff = Frame(win)
        entrystuff.grid(row=0,column=0)

        enter_label = Label(entrystuff, text="Enter Link: ")
        enter_label.pack(side=TOP)
        # define entry box here
        self.entry_link = Entry(entrystuff, width="40")
        self.entry_link.pack()

        liststuff = Frame(win)
        liststuff.grid(row=2)

        # (optional) we can add a scrollbar for listbox here
        self.listbox = Listbox(liststuff, height="30", width="50")
        self.listbox.pack()

        buttonframe= Frame(win)
        buttonframe.grid(row=1,column=0)
        buttonframe.grid_columnconfigure(4,weight=1)

        # define buttons here
        download_button = Button(buttonframe, text="Download", fg="white", bg="black")
        download_button.bind("<Button-1>", contoller.download_callback)
        download_button.grid(row=0,column=0,padx=1)

        rename_button = Button(buttonframe, text="Rename", fg="white", bg="black")
        rename_button.bind("<Button-1>", contoller.rename_window)
        #rename_button.bind("<Button-1>", contoller.download_callback)
        rename_button.grid(row=0,column=1,padx=1)

        play_button = Button(buttonframe, text="Play", fg="white", bg="green")
        play_button.grid(row=0,column=2,padx=1)

        delete_button = Button(buttonframe, text="Delete", fg="white", bg="red")
        delete_button.grid(row=0,column=3,padx=1)

    # methods are defined here (outside of __init__() )
    def insert_to_listbox(self, titles):
        """"""
        self.listbox.delete(0, END)
        for title in titles:
            self.listbox.insert(END, title)

    def get_link(self):
        """ returns the URL entered in the entry box"""
        return self.entry_link.get()
