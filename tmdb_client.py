import requests
import random


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyODA1OGEyMDMzMWE4MmFjYzk2NjMxMTczZDlkOGU4OCIsInN1YiI6IjVmMGQ3YWFlN2EzYzUyMDAzYTE3ZDM3OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9PuTn09_7LTlgIvoAMtcd5QkjKovf-bg-xZadRwOkeA"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return random.sample(data['results'], how_many)
