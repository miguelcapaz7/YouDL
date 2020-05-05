from flask import Flask, request
from youtube_video import YouTubeVideo
from youtube_manager import YouTubeManager
import json

app = Flask(__name__)

# Database File
YOUTUBE_DB = 'youtube.sqlite'

# Establishes a connection and map to the DB
youtube_mgr = YouTubeManager(YOUTUBE_DB)


@app.route('/videos', methods=['POST'])
def add_video():
    """ Adds a video to the db """
    content = request.json

    try:
        video = YouTubeVideo(content['title'], content['author'], content['resolution'],
                        content['frame_rate'], content['pathname'], content['filename'])

        video_id = youtube_mgr.add_video(video)

        response = app.response_class(
            response=str(video_id),
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response


@app.route('/videos/<string:filename>', methods=['GET'])
def get_video(filename):
    """ Gets an existing video from the YouTube Manager """

    try:
        video = youtube_mgr.get_video(filename)

        response = app.response_class(
            status=200,
            response=json.dumps(video.meta_data()),
            mimetype='application/json'
        )

        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

        return response


@app.route('/videos/all', methods=['GET'])
def get_all_videos():
    """ Gets all videos in the YouTube Manager """
    videos = youtube_mgr.get_all_videos()

    video_list = []

    for video in videos:
        video_list.append(video.meta_data())

    response = app.response_class(
        status=200,
        response=json.dumps(video_list),
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.run()