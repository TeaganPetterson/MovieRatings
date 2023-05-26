"""Server for movie ratings app."""
# table for users(user_id - primary key, email, password), 
# table for movies(serial primary key, movie_name), 
# ratings table with two foreign keys (needs user, movie, rating, and primary key)

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db, User
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

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    if user:
        flash("This email is already associated with an account, please login with password.") 
    else:
        user = crud.create_user(email, password)
        db.session.add(user) 
        db.session.commit()
        flash("Account created succesfully and you can now login.")
    return redirect ('/')

@app.route('/login', methods = ['POST'])    
def login():
    """Login user"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    print(user)
    if user:
        if password == user.password:
            session['user_id'] = user.user_id
            flash('Logged in!')
        else:
            print(user.password)
            flash("Wrong Password")

    else:
        flash("Wrong username.")
    
    return redirect('/')

@app.route('/movies')
def view_movies():
    movies = crud.get_all_movies()
    return render_template("all_movies.html", movies=movies)

@app.route('/movieDetails/<movie_id>')
def movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie, movie_id=movie_id)

@app.route ('/ratings', methods=["POST"])
    # need to ask for help, GET vs POST, URL not found,
    #  overall issues, stumped, maybe stay on the same movieDetails page
def rate_movie():
    score = request.get_json("score") 
    movie_id = int(request.get_json("movie_id")["movie_id"])
    print(f"###### Movie id: {movie_id}, type: {type(movie_id)}")
    # score = request.form.get("score")
    # movie_id = request.form.get("movie_id")
    movie = crud.get_movie_by_id(movie_id)
    movie_title = movie.title
    user = session['user_id']
    crud.create_rating(score, user, movie_id)
    flash(f'New rating added: {score} out of 5 stars to {movie_title}.')
    # return jsonify(score, movie_id)
    return jsonify({"score": score, "movie_id": movie_id})

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
