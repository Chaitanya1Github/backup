from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Books(Resource):
    def get(self):
        return {
            "books": ["Book1", "Book2", "Book3"]
        }


api.add_resource(Books, "/api/books")


# @app.route('/return_message')
# def return_message():
#     return 'the message'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
