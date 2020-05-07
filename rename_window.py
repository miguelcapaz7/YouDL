from tkinter import *


class MainWindow1(Frame):
    """ Layout for the Main Window """

    def __init__(self, parent, contoller):
        """ Initialize Main Application """
        Frame.__init__(self, parent)
        parent.title('Rename')

        self.entry_name = Entry(left_frame, width="40")
        self.entry_name.pack(side=LEFT)
