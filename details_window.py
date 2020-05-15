from tkinter import *


class DetailsWindow(Frame):

    def __init__(self, parent, video_dict):
        """ Initialize the Details window """
        Frame.__init__(self, parent)
        parent.title('Details')
        parent.configure(bg='gray15')

        self.mid_frame = Frame(self.master)
        self.mid_frame.grid(row=1, padx=30, pady=10)

        Label(self.mid_frame, text='Title:').grid(row=0, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='Author:').grid(row=1, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='Resolution:').grid(row=2, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='Frame Rate:').grid(row=3, column=0, sticky=E, padx=5, pady=5)
        Label(self.mid_frame, text='File Location:').grid(row=4, column=0, sticky=E, padx=5, pady=5)

        Label(self.mid_frame, text=video_dict['title']).grid(row=0, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['author']).grid(row=1, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['resolution']).grid(row=2, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['frame_rate'] + "fps").grid(row=3, column=1, sticky=W, padx=5, pady=5)
        Label(self.mid_frame, text=video_dict['pathname'] + video_dict['filename']).grid(row=4, column=1,
                                                                        sticky=W, padx=5, pady=5)
