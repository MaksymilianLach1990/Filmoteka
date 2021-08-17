# tworzenia połączenia z serwerem filmowym, pobieranie najpopularniejszych filmów

import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODczYzQ1MDc3YTNiOWE5ZjFhNjVlMjYyODlkYTU5MyIsInN1YiI6IjYxMTIwY" \
            "2U4MGI1ZmQ2MDA1ZWVjNjIyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zs5nesL4qjL0n2cLC_hR" \
            "tG9eGN-EiyP_Z8cm5R9NhVA"


def get_movies_list(list_type):
    categories = ["popular", "now_playing", "upcoming", "top_rated"]
    if list_type not in categories:
        list_type = 'popular'
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


# pobieranie obrazka
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    print(data)
    return data["results"][:how_many]


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


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
