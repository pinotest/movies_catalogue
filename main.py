import tmdb_client
import random
from flask import Flask, render_template, request

app = Flask(__name__)

LIST_TYPE = ['top_rated', 'upcoming', 'now_playing', 'popular']


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, LIST_TYPE=LIST_TYPE)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


@app.route('/search')
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.search_movies(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)


@app.route('/tv_series')
def tv_series():

    movies = tmdb_client.tv_series()
    return render_template("tv_series.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
