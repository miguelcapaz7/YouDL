from tkinter import *
from tkinter import ttk
import tkinter.font as font


class MainWindow(Frame):
    """ Layout for the Main Window """

    def __init__(self, parent, contoller):
        """ Initialize Main Application """
        myFont = font.Font(size=10, family='Segoe UI')
        Frame.__init__(self, parent)
        parent.title('YouDL')
        parent.configure(bg='gray15')

        # add a menu here
        main_menu = Menu(parent)
        parent.config(menu=main_menu)
        main_menu.add_command(label="Exit", command=self.quit, font=myFont)

        # define frames here
        left_frame = Frame(parent, bg='gray37')
        left_frame.pack(side=TOP)
        right_frame = Frame(parent, bg='gray15')
        right_frame.pack()
        bottom_frame = Frame(parent)
        bottom_frame.pack(side=BOTTOM)
        space_label6 = Label(bottom_frame, text="", bg='gray15')
        space_label6.pack(side=BOTTOM)
        # define labels here
        space_label7 = Label(left_frame, text="", bg='gray37')
        space_label7.pack(side=TOP)
        enter_label = Label(left_frame, text="Enter Link: ", bg='gray37', fg="white", font=myFont)
        enter_label.pack(side=LEFT)
        # define entry box here
        self.entry_link = ttk.Entry(left_frame, width="40")
        self.entry_link.pack(side=LEFT)
        space_label = Label(left_frame, text="    ", bg='gray37')
        space_label.pack(side=LEFT)
        space_label5 = Label(right_frame, text="", bg='gray15')
        space_label5.pack(side=TOP)

        # (optional) we can add a scrollbar for listbox here
        self.listbox = Listbox(right_frame, height="30", width="50")
        self.listbox.pack(side=TOP)

        # define buttons here
        download_button = Button(left_frame, text="Next", relief='flat', fg="white", bg="RoyalBlue1",
                                 command=contoller.download_win_popup, font=myFont)
        download_button.pack(side=LEFT)
        space_label2 = Label(left_frame, text=" ", bg='gray37')
        space_label2.pack(side=LEFT)

        space_label4 = Label(right_frame, text=" " * 25, bg='gray15')
        space_label4.pack(side=TOP)
        rename_button = Button(right_frame, text="Rename", relief='flat', fg="white", bg="RoyalBlue1", font=myFont)
        rename_button.bind("<Button-1>", contoller.rename_window_popup)
        rename_button.pack(side=LEFT)

        space_label3 = Label(right_frame, text=" " * 12, bg='gray15')
        space_label3.pack(side=LEFT)

        play_button = Button(right_frame, text="Play", relief='flat', fg="white", bg="green", font=myFont)
        play_button.bind("<Button-1>", contoller.play_video)
        play_button.pack(side=LEFT)

        space_label8 = Label(right_frame, text=" " * 12, bg='gray15')
        space_label8.pack(side=LEFT)

        details_button = Button(right_frame, text="Details", relief='flat', fg="white", bg="RoyalBlue1", font=myFont)
        details_button.bind("<Button-1>", contoller.details_window_popup)
        details_button.pack(side=RIGHT)

        delete_button = Button(right_frame, text="Delete", relief='flat', fg="white", bg="red", font=myFont)
        delete_button.bind("<Button-1>", contoller.delete_callback)
        delete_button.pack(side=LEFT)

        space_label5 = Label(right_frame, text="" * 25, bg='gray15')
        space_label5.pack(side=BOTTOM)

    # methods are defined here (outside of __init__() )
    def insert_to_listbox(self, titles):
        """"""
        self.listbox.delete(0, END)
        for title in titles:
            self.listbox.insert(END, title)

    def get_link(self) -> str:
        """ returns the URL entered in the entry box"""
        return self.entry_link.get()

    def get_title(self) -> str:
        """Returns the title of the active video selected"""
        title = self.listbox.get(ANCHOR)
        return title

    def get_index(self) -> int:
        """Returns the index of the active video selected"""
        index = self.listbox.index(ANCHOR)
        return index
