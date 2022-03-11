from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

# reqparse is something that brings data from form
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of a video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of a video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

videos = {}


# this function handles error when key in dictionary does not exist
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="video_id does not exist...")


# this function handles error key in dictionary already exists, so you cannot added any new in it.
def abort_if_video_id_exists(video_id):
    if video_id in videos:
        abort(409, message="video_id already exists...")


class Video(Resource):
    # we getting the data based on video_id, but if video_id does not exist then KeyError is thrown.
    # this error is handled by "abort()"
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        # below function will abort as soon as video_id is found in dictionary
        abort_if_video_id_exists(video_id)
        # get the data from URL in args
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        # if video_id does not exist then it wll abort otherwise it will move to next line below
        abort_if_video_id_doesnt_exist(video_id)

        del videos[video_id]
        return "", 204

# when ever you create any resource, you need to come here and register that resource
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)

