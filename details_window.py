from tkinter import *
import tkinter.font as font


class DetailsWindow(Frame):

    def __init__(self, parent, video_dict):
        """ Initialize the Details window """
        Frame.__init__(self, parent)
        parent.title('Details')
        parent.configure(bg='gray15')
        myFont = font.Font(size=10, family='Segoe UI')

        self.mid_frame = Frame(self.master, bg='gray15')
        self.mid_frame.grid(row=1, padx=30, pady=10)

        Label(self.mid_frame, text='Title:', bg='gray15', fg='white', font=myFont)\
            .grid(row=0, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='Author:', bg='gray15', fg='white', font=myFont)\
            .grid(row=1, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='Resolution:', bg='gray15', fg='white', font=myFont)\
            .grid(row=2, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='Frame Rate:', bg='gray15', fg='white', font=myFont)\
            .grid(row=3, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='File Location:', bg='gray15', fg='white', font=myFont)\
            .grid(row=4, column=0, sticky=E, padx=5, pady=5)

        Label(self.mid_frame, text=video_dict['title'], bg='gray15', fg='white', font=myFont)\
            .grid(row=0, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['author'], bg='gray15', fg='white', font=myFont)\
            .grid(row=1, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['resolution'], bg='gray15', fg='white', font=myFont)\
            .grid(row=2, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['frame_rate'] + "fps", bg='gray15', fg='white', font=myFont)\
            .grid(row=3, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['pathname'] + video_dict['filename'], bg='gray15',
              fg='white', font=myFont).grid(row=4, column=1, sticky=W, padx=5, pady=5)
