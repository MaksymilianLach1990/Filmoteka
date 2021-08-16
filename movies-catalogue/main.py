from flask import Flask, render_template, request
import random
import tmdb_client

app = Flask(__name__)
app.config["ENV"] = "development"


@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=8)  # lista filmów / ilość okienek
    return render_template("homepage.html", movies=movies)  # strona głowna


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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("contact.html")  # strona odpowiadąca za "contact"


if __name__ == '__main__':
    app.run(debug=True)
