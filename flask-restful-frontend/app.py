import json

from Tools.scripts.make_ctype import method
from bson import ObjectId, json_util
from flask import Flask, request, render_template, url_for
import requests
from werkzeug.utils import redirect

from database import db

app = Flask(__name__)
# http://127.0.0.1:5000/book/book1


@app.route('/')
def all_book():
    documents = list(db.microservice_collection.find({}))
    print(documents)
    return render_template("show_books.html", documents=documents)


@app.route('/book/<book_id>')
def get_book(book_id):
    book = requests.get('http://127.0.0.1:5000/book/' + book_id)
    # print(book.json())
    return book.json()


# @app.route('/add_book', defaults={"book_id": None}, methods=["GET", "POST"])
@app.route('/book/add_book', methods=["GET", "POST"])
def add_book():

    if request.method == 'POST':

        data = {
            "new_book": {"book_name": request.form["book_name"], "author_name": request.form["author_name"]},
        }

        response = requests.put("http://127.0.0.1:5000/book/add_book", data["new_book"])
        return redirect(url_for('.all_book'))

    return render_template("add_book.html")


@app.route('/book/update_book/<book_id>', methods=["GET", "POST"])
def update_book(book_id):
    if request.method == 'POST':
        data = {
            "new_book": {"book_name": request.form["book_name"], "author_name": request.form["author_name"]},
        }

        response = requests.patch('http://127.0.0.1:5000/book/update_book/' + book_id, data["new_book"])
        # print(response.json())
        return redirect(url_for('.all_book'))

    _id = book_id
    document = list(db.microservice_collection.find({"_id": ObjectId(_id)}))[0]
    return render_template("update_book.html", document=document)


@app.route('/book/delete_book/<book_id>', methods=["GET", "POST"])
def delete_book(book_id):
    response = requests.delete('http://127.0.0.1:5000/book/delete_book/' + book_id)
    # print(response.json())
    return redirect(url_for('.all_book'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
