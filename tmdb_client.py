import requests
import random
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyODA1OGEyMDMzMWE4MmFjYzk2NjMxMTczZDlkOGU4OCIsInN1YiI6IjVmMGQ3YWFlN2EzYzUyMDAzYTE3ZDM3OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9PuTn09_7LTlgIvoAMtcd5QkjKovf-bg-xZadRwOkeA"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return random.sample(data['results'], how_many)


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]
