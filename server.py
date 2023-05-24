"""Server for movie ratings app."""
# table for users(user_id - primary key, email, password), 
# table for movies(serial primary key, movie_name), 
# ratings table with two foreign keys (needs user, movie, rating, and primary key)

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """Fucntions if needed"""
    return render_template("homepage.html")

@app.route('/movies')
def view_movies():
    movies = crud.get_all_movies()
    return render_template("all_movies.html", movies=movies)

@app.route('/movieDetails/<movie_id>')
def movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)

@app.route ('/users')
def view_users():
    users = crud.get_all_users()
    return render_template("all_users.html", users=users)

@app.route('/userDetails/<user_id>')
def user_details(user_id):
    user= crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=3000)
