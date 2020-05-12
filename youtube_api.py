from youtube_video import YouTubeVideo
from youtube_manager import YouTubeManager

# Database File
YOUTUBE_DB = 'youtube.sqlite'

# Establishes a connection and map to the DB
youtube_mgr = YouTubeManager(YOUTUBE_DB)


class YouTubeAPI:
    """Receives data from controller and communicates with DB"""

    def __init__(self):
        """Define properties for YouTubeAPI class"""
        self.youtube_mgr = youtube_mgr

    def add_video(self, video_dict):
        """ Adds a video to the db """
        content = video_dict

        try:
            video = YouTubeVideo(content['title'], content['author'], content['resolution'],
                                 content['frame_rate'], content['pathname'], content['filename'])
            video_id = self.youtube_mgr.add_video(video)

            response = str(video_id)
        except ValueError as e:
            response = str(e)

        return response

    def update_title(self, form_data, filename):
        """ Updates the title in YouTube Manager """
        content = form_data

        try:
            video = self.youtube_mgr.get_video(filename)
            if 'title' in content.keys():
                video.title = content['title']
            self.youtube_mgr.update_video(video)

            response = 200
        except ValueError as e:
            response = str(e)

        return response

    def get_video(self, filename):
        """ Gets an existing video from the YouTube Manager """

        try:
            video = self.youtube_mgr.get_video(filename)

            response = video.meta_data()

            return response
        except ValueError as e:
            response = str(e)

            return response

    def get_all_videos(self):
        """ Gets all videos in the YouTube Manager """
        videos = self.youtube_mgr.get_all_videos()

        video_list = []

        for video in videos:
            video_list.append(video.meta_data())

        response = video_list

        return response

    def delete_video(self, filename):
        """ Delete an existing video from the YouTube Manager """
        try:
            self.youtube_mgr.delete_video(filename)
            response = 200

        except ValueError as e:
            response = str(e)

        return response
