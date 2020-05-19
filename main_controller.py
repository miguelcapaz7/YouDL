from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from main_window import MainWindow
from rename_window import RenameWindow
from details_window import DetailsWindow
from download_window import DownloadWindow
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

    def download_callback(self):
        """Downloads a YouTube video with the specified URL
        Posts the video data to the API"""
        yt = self.download.yt_obj
        try:
            if self.download.format_label['text'] != "mp3":
                path = self.__validate_path()
                res = self.__validate_res()
                format = self.__validate_format()
                fps = self.__validate_fps()
                streams_list = self.__validate_video(yt, format, res, fps)
                video = streams_list[0]
                # Checks if the file already exists in the directory
                for clip in self.youtube_api.get_all_videos():
                    file, extension = clip['filename'].split(".")
                    if yt.title == clip['title'] and yt.author == clip['author'] and \
                            path == clip['pathname'] and extension == format:
                        raise ValueError("File already exists")
                file_location = video.download(path)

                data = {'title': yt.title,
                        'author': yt.author,
                        'resolution': video.resolution,
                        'frame_rate': video.fps,
                        'pathname': path,
                        'filename': os.path.basename(file_location)
                        }

                response = self.youtube_api.add_video(data)
                msg = "Your video has been downloaded"
                messagebox.showinfo(title="Downloaded", message=msg)
                self.download_win.destroy()
                self.list_titles_callback()
            else:
                streams_list, path = self.__validate_audio(yt)
                video = streams_list[0]
                for clip in self.youtube_api.get_all_videos():
                    if yt.title == clip['title'] and yt.author == clip['author'] \
                            and path == clip["pathname"]:
                        raise ValueError("File already exists")
                file_location = video.download(path)
                file_name, extension = os.path.basename(file_location).split(".")
                file = file_name + ".mp3"
                os.rename(file_location, path + file)

                data = {'title': yt.title,
                        'author': yt.author,
                        'resolution': video.resolution,
                        'frame_rate': video.fps,
                        'pathname': path,
                        'filename': file
                        }
                response = self.youtube_api.add_video(data)
                msg = "Your video has been downloaded"
                messagebox.showinfo(title="Downloaded", message=msg)
                self.download_win.destroy()
                self.list_titles_callback()
        except ValueError as e:
            messagebox.showinfo(title="Error", message=str(e))

    def __validate_path(self) -> str:
        """Checks if a path is chosen"""
        path = self.download.file_label['text']
        if path == "":
            raise ValueError("Pick a file location.")
        return path

    def __validate_res(self) -> str:
        """Checks if a resolution is chosen"""
        res = self.download.res_label['text']
        if res == "":
            raise ValueError("Pick a resolution")
        return res

    def __validate_format(self) -> str:
        """Checks if a format is chosen"""
        format = self.download.format_label['text']
        if format == "":
            raise ValueError("Pick a file format")
        return format

    def __validate_fps(self) -> str:
        """Checks if fps is chosen"""
        fps = self.download.fps_label['text']
        if fps == "":
            raise ValueError("Pick fps")
        return fps

    def __validate_video(self, yt, format, res, fps) -> list:
        """Validates streams for videos"""
        try:
            streams_list = []
            for stream in yt.streams:
                type, extension = stream.mime_type.split("/")
                if extension == format and stream.resolution == res and stream.fps == fps:
                    streams_list.append(stream)
            if len(streams_list) < 1:
                raise ValueError
            return streams_list
        except Exception:
            msg = "This format is not available. Try picking another format."
            messagebox.showinfo(title="Error", message=msg)

    def __validate_audio(self, yt):
        """Validates streams for audio"""
        format = self.download.format_label['text']
        path = self.download.file_label['text']
        if path == "":
            raise ValueError("Pick a file location.")
        streams_list = []
        for stream in yt.streams:
            type, old_extenstion = stream.mime_type.split("/")
            if type == "audio":
                new_extention = old_extenstion.replace(old_extenstion, "mp3")
                if new_extention == format:
                    streams_list.append(stream)
        return streams_list, path

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

    def details_window_popup(self, event):
        """Launches a window with the video details listed"""
        if self._main_window.get_title() == "":
            msg_str = "You must select a video first."
            messagebox.showinfo(title="Error", message=msg_str)
        else:
            index = self._main_window.get_index()
            video_list = self.youtube_api.get_all_videos()
            video = video_list[index]
            self.details_win = tk.Toplevel()
            self.details = DetailsWindow(self.details_win, video)

    def download_win_popup(self):
        """Launches the Download settings window"""
        try:
            yt_obj = YouTube(self._main_window.get_link())
            self.download_win = tk.Toplevel()
            self.download = DownloadWindow(self.download_win, self, yt_obj)
        except Exception:
            msg_str = "Please paste a valid YouTube URL"
            messagebox.showinfo(title="Error", message=msg_str)

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

            response = self.youtube_api.update_title(form_data, video['pathname'], video['filename'])

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
            del_response = self.youtube_api.delete_video(video['pathname'], filename)

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
