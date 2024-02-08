from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models.movies_model import MoviesModel
from config.db import collection_movies
from schemas.movies_schema import list_serial_movies
from bson import ObjectId

moviesRouter = APIRouter()

# Get all movies
@moviesRouter.get("/movies")
async def get_all_movies():
    movies = list_serial_movies(collection_movies.find())
    if not movies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No movies found")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data":movies, "message": "Movies load successfully"})


# Add a new movie
@moviesRouter.post("/movies")
async def add_movie(movies: MoviesModel):
    try:
        result = collection_movies.insert_one(dict(movies))
        if not result.inserted_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add movie")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {
        "status": "OK",
        "message": "Movie added successfully."
    }


# Get a movie by id
@moviesRouter.get("/movies/{id}")
async def get_movie_by_id(id):
    movie = list_serial_movies(collection_movies.find({"_id": ObjectId(id)}))
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return movie

# Update a movie by id
@moviesRouter.put("/movies/{id}")
async def update_movie_by_id(id:str, movies: MoviesModel):
    try:
        result = collection_movies.update_one({"_id": ObjectId(id)}, {"$set": dict(movies)})
        if not result.modified_count:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update movie")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {
        "status": "OK",
        "message": "Movie updated successfully."
    }

# Delete a movie by id
@moviesRouter.delete("/movies/{id}")
async def delete_movie_by_id(id):
    try:
        result = collection_movies.delete_one({"_id": ObjectId(id)})
        if not result.deleted_count:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete movie")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return {
        "status": "OK",
        "message": "Movie deleted successfully."
    }