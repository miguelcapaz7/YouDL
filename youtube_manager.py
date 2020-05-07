from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from youtube_video import YouTubeVideo
from base import Base


class YouTubeManager:

    def __init__(self, youtube_db):
        """ Creates a YouTubeVideo object and map to the Database """

        if youtube_db is None or youtube_db == "":
            raise ValueError(f"YouTube database [{youtube_db}] not found")

        engine = create_engine('sqlite:///' + youtube_db)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_video(self, new_video: YouTubeVideo):
        """ Adds a new YouTubeVideo to the youtube database """

        if new_video is None or not isinstance(new_video, YouTubeVideo):
            raise ValueError("Invalid YouTube Object")

        for video in self.get_all_videos():
            if new_video.title == video.title and new_video.author == video.author:
                raise ValueError("Video already exists")

        session = self._db_session()
        session.add(new_video)

        session.commit()

        song_id = new_video.title + " has been added"
        session.close()

        return song_id

    def update_video(self, video):
        """ Updates the title and stores in DB """

        if video is None or not isinstance(video, YouTubeVideo):
            raise ValueError("Invalid YouTube Object")

        session = self._db_session()

        existing_video = session.query(YouTubeVideo).filter(
            YouTubeVideo.id == video.id).first()
        if existing_video is None:
            raise ValueError("YouTube Video does not exist")
        existing_video.update_title(video)
        session.commit()
        session.close()

    def get_video(self, filename):
        """ Return YouTubeVideo object matching ID"""
        if filename is None or type(filename) != str:
            raise ValueError("Invalid Filename")

        session = self._db_session()

        for video in self.get_all_videos():
            if filename == video.filename:
                session.close()
                return video

    def get_all_videos(self):
        """ Return a list of all videos in the DB """
        session = self._db_session()

        all_videos = session.query(YouTubeVideo).all()

        session.close()

        return all_videos

    def delete_video(self, filename):
        """ Deletes a video from the database """
        if filename is None or type(filename) != str:
            raise ValueError("Invalid Filename")

        session = self._db_session()

        for video in self.get_all_videos():
            if video is None:
                session.close()
                raise ValueError("Video does not exist")

            if filename == video.filename:
                session.delete(video)
                session.commit()

                session.close()
