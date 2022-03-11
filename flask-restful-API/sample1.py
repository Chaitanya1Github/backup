from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

names = {
    "kabir": {"age": 26, "city": "pune"},
    "chaitanya": {"age": 30, "city": "mumbai"},
}

# create a resource.
# Resource is nothing but a class.
# when HelloWorld extends from Resource, HelloWorld becomes Resource.
# After that we override different methods in Resource AKA HelloWorld.
class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "I`m POST"}



# when ever you create any resource, you need to come here and register that resource
api.add_resource(HelloWorld, "/hello_world/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)

