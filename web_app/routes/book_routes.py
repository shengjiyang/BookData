# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
from ..models import Book, db

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Dune"},
        {"id": 2, "title": "Dune Messiah"},
        {"id": 3, "title": "Children of Dune"},
    ]
    return jsonify(books)



@book_routes.route("/books")
def list_books_for_humans():
    # books = [
    #     {"id": 1, "title": "Dune"},
    #     {"id": 2, "title": "Dune Messiah"},
    #     {"id": 3, "title": "Children of Dune"},
    # ]

    # SELECT * FROM books;
    book_records = Book.query.all()
    print(book_records)

    return render_template("books.html", message="Here are some books!", books=book_records)


@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    # INSERT INTO books...
    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    return redirect("/books")

# @book_routes.route("/books/create", methods=["POST"])
# def create_book():
#     print("FORM DATA:", dict(request.form))

#     return jsonify({
#         "message" : "BOOK CREATED",
#         "title" : dict(request.form)
#     })