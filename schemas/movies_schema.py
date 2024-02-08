def individual_serial_movies(movies: dict) -> dict:
    return {
        "id": str(movies["_id"]),
        "mName": movies["mName"],
        "mYear": movies["mYear"],
        "mCategory": movies["mCategory"],
        "mDuration": movies["mDuration"],
        "mLanguage": movies["mLanguage"],
        "mDirector": movies["mDirector"],
    }

def list_serial_movies(movies) -> list:
    return [individual_serial_movies(movie) for movie in movies]
