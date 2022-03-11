from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# it is just the location where you want to save the database file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.db"
db = SQLAlchemy(app)


# we are creating table and fields for table (just like ORM model in django)
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    # this method is used to represent something you return, still you can check the use of __repr__
    def __repr__(self, name, views, likes):
        return f"Video(name = {name}, views = {views}, likes = {likes})"


# this command will create new database, so you need to run this only once, otherwise it will override your database
# the moment you run this file, you will .db file, then you want to comment the line below
# db.create_all()


# reqparse is something that brings data from form
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of a video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of a video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

# creating reqparse for update request
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of a video is required")
video_update_args.add_argument("views", type=int, help="Views of a video is required")
video_update_args.add_argument("likes", type=int, help="Likes on the video is required")


# this is a normal dictionary. But in this we are using 'fields', which is like creating a structure for an object to serialized in this particular way.
# it is used as: 'marshal_with(resource_fields)'
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}


class Video(Resource):
    # marshal_with() takes the returned value/object(id, name, views, likes) by this method and serializes it and the pattern of serializing is defined in resource_fields
    @marshal_with(resource_fields)
    def get(self, video_id):
        # now when you get a data, it is essentially an object.
        # now in order for "response" in test.py to read the return object, we need to make it serialized(in short, something that is in json format)
        # in order make is serializeable we use something called 'marshal_with()' and 'fields'
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find video with that id')
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        # if this id already exists then control must be aborted
        # it is just a way to handle errors using abort()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="this video id is taken...")

        # received data from URL
        args = video_put_args.parse_args()

        # created instance of class VideoModel().
        # when the instance is saved, new record will be added in database
        video = VideoModel(id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        # saves temporarily
        db.session.add(video)
        # saves permanently
        db.session.commit()

        # here you return 'video' as an object/instance, if you want it to be read only then you need marshal_with(), otherwise you don`t.
        return video, 201

    # this method is used to update
    # always remember the return value by this function is checked against the resource_fields and the resource_fields are returned finally.
    # though you try to return anything when used marshal_with() it wont work, any returned value will always be in the form of resource_fields
    @marshal_with(resource_fields)
    def patch(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find video with that id, cannot update')

        # fetch data from URL but following rules set in video_update_args
        args = video_update_args.parse_args()

        if args['name'] and args['name'] is not None:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

    # here we dont need marshal_with() becausewe are not returning anything in the end
    @marshal_with(resource_fields)
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find video with that id, cannot update')
        VideoModel.query.filter_by(id=video_id).delete()
        db.session.commit()
        return "deleted", 204

# when ever you create any resource, you need to come here and register that resource
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)

