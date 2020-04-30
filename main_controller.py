from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from main_window import MainWindow
import os


class MainController(tk.Frame):
    """
    Controller for our views
    """

    def __init__(self, parent):
        """Creates the main window"""
        tk.Frame.__init__(self, parent)
        # creates an instance of the MainWindow class
        self._root_win = tk.Toplevel()
        self._main_window = MainWindow(self._root_win, self)

        # defines a list to add all of the downloaded video titles
        self._video_titles = []

        # call this function to add all the names to the list at startup
        self.list_titles_callback()

    def download_callback(self):
        """Downloads a YouTube video with the specified URL"""
        link = self._main_window.get_link()  # returns the input from the entry box
        yt = YouTube(link)  # creates a YouTube object
        video = yt.streams.first()  # chooses the first format available
        file_location = video.download(os.getcwd() +
                                   "\\YouTube_Downloads")  # downloads the video to the
                                                            # specified directory

        msg = yt.title, " has been downloaded."
        messagebox.showinfo(title="Downloaded", message=msg)
        self.list_titles_callback()

    def list_titles_callback(self):
        """ Lists video titles in listbox.
        Currently, this is reading the files from the YouTube Downloads directory.
        We are going to change this so it reads the titles from the database (sprint 2)"""
        self._video_titles.clear()  # removes all items in the list

        # adds all the downloaded files to the video_titles list
        for video_file in os.listdir(os.getcwd() + "\\YouTube_Downloads"):
            video_file.split(".")
            title = video_file[0]
            self._video_titles.append(title)

        # inserts the titles to the tkinter listbox
        self._main_window.insert_to_listbox(self._video_titles)


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainController(root).pack()
    tk.mainloop()