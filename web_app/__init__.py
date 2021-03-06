# web_app/__init__.py

from flask import Flask

from web_app.models import db, migrate

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

DATABASE_URI = "sqlite:////Users/samuel/Programming/GitHub/Lambda School/Assignments/BookData/book_database.db" # using absolute filepath on Mac (recommended)

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)