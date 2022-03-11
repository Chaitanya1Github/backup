import json

from bson import ObjectId, json_util
from flask import request

from flask import Flask
from flask_restful import Resource, Api, reqparse

from database import db

app = Flask(__name__)
api = Api(app)

book_put_args = reqparse.RequestParser()
book_put_args.add_argument("book_name", type=str, help="Book name is required", required=True)
book_put_args.add_argument("author_name", type=str, help="Author name is required", required=True)

book_update_args = reqparse.RequestParser()
book_update_args.add_argument("book_name", type=str, help="Book name is required", required=True)
book_update_args.add_argument("author_name", type=str, help="Author name is required", required=True)


class Book(Resource):

    # get specific book
    def get(self, book_id):
        _id = book_id
        document = list(db.microservice_collection.find({"_id": ObjectId(_id)}))[0]
        return json.loads(json_util.dumps(document))

    def put(self):
        args = book_put_args.parse_args()
        db.microservice_collection.insert_one({"book_name": args["book_name"], "author_name": args["author_name"]})
        print(args)
        return args

    def patch(self, book_id):
        _id = book_id
        document = list(db.microservice_collection.find({"_id": ObjectId(_id)}))[0]
        args = book_update_args.parse_args()
        set_new_data = {
            "$set": {
                "book_name": args["book_name"],
                "author_name": args["author_name"],
            }
        }
        db.microservice_collection.update_many(document, set_new_data)
        return "args"

    def delete(self, book_id):
        _id = book_id
        document = list(db.microservice_collection.find({"_id": ObjectId(_id)}))[0]
        db.microservice_collection.delete_one(document)
        return "deleted successfully"


# first endpoint: get data when Id is passed
# second endpoint: add data with no requirement of Id
# patch/update
# delete

api.add_resource(Book, '/book/<book_id>', '/book/add_book', '/book/update_book/<book_id>', '/book/delete_book/<book_id>')

if __name__ == "__main__":
    app.run(debug=True)

