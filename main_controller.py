from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from main_window import MainWindow
from rename_window import RenameWindow
from youtube_api import YouTubeAPI
import os


class MainController(tk.Frame):
    """
    Controller for our views
    """

    def __init__(self, parent):
        """Creates the main window"""
        tk.Frame.__init__(self, parent)
        # creates an instance of YouTubeAPI
        self.youtube_api = YouTubeAPI()
        # creates an instance of the MainWindow class
        self._root_win = tk.Toplevel()
        self._main_window = MainWindow(self._root_win, self)

        # defines a list to add all of the downloaded video titles
        self._video_titles = []

        # call this function to add all the names to the list at startup
        self.list_titles_callback()

    def download_callback(self, event):
        """Downloads a YouTube video with the specified URL
        Posts the video data to the API"""
        link = self._main_window.get_link()  # returns the input from the entry box
        if link == "":
            msg = "Please enter a valid YouTube URL"
            messagebox.showinfo(title="Error", message=msg)
        else:
            yt = YouTube(link)  # creates a YouTube object
            video = yt.streams.first()  # chooses the first format available
            file_location = video.download(os.getcwd() +
                                           "\\YouTube_Downloads")  # downloads the video to the
                                                                    # specified directory

            # creates a dictionary with the videos properties
            data = {'title': yt.title,
                    'author': yt.author,
                    'resolution': video.resolution,
                    'frame_rate': video.fps,
                    'pathname': os.getcwd() + "\\YouTube_Downloads\\",
                    'filename': os.path.basename(file_location)
                    }

            # sends data to API
            response = self.youtube_api.add_video(data)
            messagebox.showinfo(title="Downloaded", message=response)
            self.list_titles_callback()

    def list_titles_callback(self):
        """ Lists video titles in listbox.
        Gets all the videos stored in the database and adds the title"""
        self._video_titles.clear()  # removes all items in the list

        # calls API and returns a list of videos
        video_list = self.youtube_api.get_all_videos()
        for video in video_list:
            self._video_titles.append(video['title'])

        # inserts the titles to the tkinter listbox
        self._main_window.insert_to_listbox(self._video_titles)

    def play_video(self, event):
        """Plays the selected video"""
        index = self._main_window.get_index()
        if self._main_window.get_title() == "":
            msg_str = "You must select a video first."
            messagebox.showinfo(title="Error", message=msg_str)
        else:
            video_list = self.youtube_api.get_all_videos()
            video = video_list[index]
            file_location = video['pathname'] + video['filename']
            os.startfile(file_location)

    def rename_window_popup(self, event):
        """Launches the Rename Window"""
        title = self._main_window.get_title()
        if title == "":
            msg_str = "You must select a video first to rename."
            messagebox.showinfo(title="Error", message=msg_str)
        else:
            self.rename_win = tk.Toplevel()
            self.rename = RenameWindow(self.rename_win, self, title)

    def update_title(self, event):
        """Updates the title of the video - sends request to API"""
        index = self._main_window.get_index()
        form_data = self.rename.get_form_data()
        if form_data['title'] == "":
            message = "Field cannot be left empty"
            messagebox.showinfo(title="Error", message=message)
        else:
            video_list = self.youtube_api.get_all_videos()
            video = video_list[index]

            response = self.youtube_api.update_title(form_data, video['filename'])

            if response == 200:
                message = "Video Title has been updated"
                messagebox.showinfo(title="Video Updated", message=message)
                self.rename_win.destroy()
                self.list_titles_callback()
            else:
                message = response
                messagebox.showinfo(title="Error", message=message)

    def delete_callback(self, event):
        """ Deletes selected video from the library. """
        index = self._main_window.get_index()  # returns index of title in listbox
        if self._main_window.get_title() == "":  # checks if you selected a video before deleting
            msg_str = "You must select a video first."
            messagebox.showinfo(title="Error", message=msg_str)
        else:
            # gets a list of all the videos in the database
            video_list = self.youtube_api.get_all_videos()
            video = video_list[index]  # gets the specific video you chose
            filename = video['filename']

            # sends a delete request to the API
            del_response = self.youtube_api.delete_video(filename)

            if del_response == 200:
                msg_str = video['title'] + " has been deleted from library"
                messagebox.showinfo(title="Video Deleted", message=msg_str)
                self.list_titles_callback()
                os.remove(video['pathname'] + filename)
            else:
                msg_str = del_response
                messagebox.showinfo(title="Error", message=msg_str)


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainController(root).pack()
    tk.mainloop()
