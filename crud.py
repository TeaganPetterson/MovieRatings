"""CRUD operations."""
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_all_users():
    users = User.query.all()
    return users
    
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user


def create_movie(title, overview, release_date, poster_path):
    """Create a movie"""

    movie = Movie(title=title, overview=overview, release_date= release_date, poster_path=poster_path)

    return movie

def get_all_movies():
    movies = Movie.query.all()
    return movies

def get_movie_by_id(movie_id):
    movie = Movie.query.get(movie_id)
    return movie

def create_rating(score, user_id, movie_id):
    """Create a new rating"""
    rating = Rating(score=score, user_id=user_id, movie_id=movie_id)
    return rating

def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)