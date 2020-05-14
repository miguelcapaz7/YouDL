from sqlalchemy import Column, Text, Integer
from base import Base
import os


class YouTubeVideo(Base):
    """Represents a YouTube Video"""

    """ ORM: map db columns to instance variables in this class """

    __tablename__ = "YouTubeVideo"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    resolution = Column(Text)
    frame_rate = Column(Text)
    pathname = Column(Text, nullable=False)
    filename = Column(Text, nullable=False)

    def __init__(self, title: str, author: str, resolution: str, frame_rate: str,
                 pathname: str, filename: str):
        """This is the constructor that creates a youtube instance"""

        self.title = title
        self.author = author
        self.resolution = resolution
        self.frame_rate = frame_rate

        if not YouTubeVideo.__validate_filepath(pathname, filename):
            raise ValueError("The file path cannot be found.")
        else:
            self.pathname = pathname
            self.filename = filename

    def update_title(self, video):
        """Updates the name of the title to the database"""
        self.title = video.title

    def meta_data(self) -> dict:
        """Returns a dictionary of the YouTube video details"""
        video_dict = {
            "title": self.title,
            "author": self.author,
            "resolution": self.resolution,
            "frame_rate": self.frame_rate,
            "pathname": self.pathname,
            "filename": self.filename
        }
        return video_dict

    @classmethod
    def __validate_filepath(cls, pathname, filename) -> bool:
        """Validates that the path exists"""
        if os.path.exists(pathname + filename):
            return True
        else:
            return False

