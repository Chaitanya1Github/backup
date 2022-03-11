# In docker-compose "books" is a service, which is a container.
# this container has some IP address.
# while calling URL we need IP address, but you dont know its IP.
# So what you can do is http://books:8000/
# this will send an api request

from flask import Flask
import requests

app = Flask(__name__)


@app.route('/get_message')
def get_message():
    message = requests.get('http://books:5000/return_message')
    return message.text


if __name__ == '__main__':
    app.run(host='0.0.0.0')
