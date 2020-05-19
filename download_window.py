from tkinter import *
from tkinter import filedialog
import tkinter.font as font


class DownloadWindow(Frame):

    """Window that shows the video settings for the download"""

    def __init__(self, parent, controller, yt_obj):
        """ Initialize the Settings window """
        Frame.__init__(self, parent)
        parent.title('Choose Format')
        parent.configure(bg='gray15')
        myFont = font.Font(size=10, family='Segoe UI')

        self.yt_obj = yt_obj

        self.top_frame = Frame(self.master, bg='gray15')
        self.mid_frame = Frame(self.master, bg='gray15')
        self.bot_frame = Frame(self.master, bg='gray15')
        self.top_frame.grid(row=0, padx=10)
        self.mid_frame.grid(row=1, padx=10)
        self.bot_frame.grid(row=2, padx=30, pady=10)

        Label(self.top_frame, text="Choose your download settings", bg='gray15', fg='white', font=myFont) \
            .grid(row=0, column=0, sticky=N)

        self.format_listbox = Listbox(self.mid_frame, width=12, height=8)
        self.format_listbox.grid(row=1, column=1)

        self.res_listbox = Listbox(self.mid_frame, width=12, height=8)
        self.res_listbox.grid(row=1, column=0)

        self.fps_listbox = Listbox(self.mid_frame, width=12, height=8)
        self.fps_listbox.grid(row=1, column=2)

        Label(self.bot_frame, text="Choose a location for your download", bg='gray15', fg='white', font=myFont) \
            .grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.browse_button = Button(self.bot_frame, text='Browse', width=10, command=self.get_chosen_path,
                                    bg='RoyalBlue1', fg='white', font=myFont)
        self.browse_button.grid(row=1, column=0)

        self.file_label = Label(self.bot_frame, text="", bg='gray15', fg='white', font=myFont)
        self.file_label.grid(row=2, column=0)

        self.res_label = Label(self.mid_frame, text="", bg='gray15', fg='white', font=myFont)
        self.res_label.grid(row=3, column=0)

        self.format_label = Label(self.mid_frame, text="", bg='gray15', fg='white', font=myFont)
        self.format_label.grid(row=3, column=1)

        self.fps_label = Label(self.mid_frame, text="", bg='gray15', fg='white', font=myFont)
        self.fps_label.grid(row=3, column=2)

        self.res_button = Button(self.mid_frame, text='Resolution', width=9, command=self.get_res,
                                 bg='RoyalBlue1', fg='white', font=myFont)
        self.res_button.grid(row=2, column=0)

        self.format_button = Button(self.mid_frame, text='Format', width=9, command=self.get_format,
                                    bg='RoyalBlue1', fg='white', font=myFont)
        self.format_button.grid(row=2, column=1)

        self.fps_button = Button(self.mid_frame, text='FPS', width=9, command=self.get_fps,
                                 bg='RoyalBlue1', fg='white', font=myFont)
        self.fps_button.grid(row=2, column=2)

        self.download = Button(self.bot_frame, text='Download', width=10, command=controller.download_callback,
                               bg='RoyalBlue1', fg='white', font=myFont)
        self.download.grid(row=3, column=0)

        self.insert_formats_to_listbox()
        self.insert_resolution_to_listbox()
        self.insert_fps_to_listbox()

    def insert_formats_to_listbox(self):
        """Inserts available file formats to the listbox"""
        self.format_listbox.delete(0, END)
        format_list = []
        format_list.clear()
        for stream in self.yt_obj.streams:
            format = stream.mime_type.split("/")
            extension = format[1]
            if format[0] == "audio":
                extension = "mp3"
            if extension not in format_list:
                format_list.append(extension)
                self.format_listbox.insert(END, extension)

    def insert_resolution_to_listbox(self):
        """Inserts available resolutions to the listbox"""
        self.res_listbox.delete(0, END)
        res_list = []
        res_list.clear()
        for stream in self.yt_obj.streams:
            resolution = stream.resolution
            if resolution not in res_list:
                res_list.append(resolution)
                self.res_listbox.insert(END, resolution)

    def insert_fps_to_listbox(self):
        """Inserts available fps to the listbox"""
        self.fps_listbox.delete(0, END)
        fps_list = []
        fps_list.clear()
        for stream in self.yt_obj.streams:
            fps = stream.fps
            if fps not in fps_list:
                fps_list.append(fps)
                self.fps_listbox.insert(END, fps)

    def get_fps(self):
        """Returns the selected fps"""
        self.fps_label['text'] = self.fps_listbox.get(ANCHOR)

    def get_res(self):
        """Returns the selected resolution"""
        self.res_label['text'] = self.res_listbox.get(ANCHOR)

    def get_format(self):
        """Returns the selected format"""
        self.format_label['text'] = self.format_listbox.get(ANCHOR)
        if self.format_label['text'] == "mp3":
            self.res_listbox.delete(0, END)
            self.fps_listbox.delete(0, END)
            self.res_label['text'] = ""
            self.fps_label['text'] = ""
        else:
            self.insert_resolution_to_listbox()
            self.insert_fps_to_listbox()

    def get_chosen_path(self):
        """Returns the directory selected"""
        chosen_path = filedialog.askdirectory()
        path = str(chosen_path).replace("/", "\\")
        self.file_label['text'] = str(path) + "\\"
