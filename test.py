from unittest import TestCase
import inspect
import tkinter as tk
from main_controller import MainController
from main_window import MainWindow
from youtube_manager import YouTubeManager
from youtube_video import YouTubeVideo


class TestFunctions(TestCase):

    def setUp(self):
        """This is for Url data objects"""
        self._youtube_manager = YouTubeManager('youtube.sqlite')
        self.main_controller = MainController(tk.Tk())
        self._url1 = "https://www.youtube.com/watch?v=2ZIpFytCSVc"
        self._url2 = "https://www.youtube.com/watch?v=6TWJaFD6R2s"

    def tearDown(self):
        self.log()

    def log(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_download_event(self):
        """Testing the Download Callback Function """
        self.assertTrue(self.main_controller.list_titles_callback)

    def test_list_callback(self):
        """Testing the List Callback when """
        self.assertTrue(self.main_controller.download_callback)

    def test_play_video(self):
        """Testing the play_video function"""
        self.assertTrue(self.main_controller.play_video)

    def test_rename_window_popup(self):
        """Testing the rename window pop up"""
        self.assertTrue(self.main_controller.rename_window_popup)

    def test_download_win_popup(self):
        """Testing the download window popup"""
        self.assertTrue(self.main_controller.download_win_popup)

    def test_delete_callback(self):
        """Testing the delete bacllback"""
        self.assertTrue(self.main_controller.delete_callback)

    def test_update_title(self):
        """Testing the update title function"""
        self.assertTrue(self.main_controller.update_title)

    # def Test_Youtube_api(self):
    #     """Testing the youtube Api"""

