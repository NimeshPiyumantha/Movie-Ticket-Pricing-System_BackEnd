from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.movies_routes import moviesRouter
from routes.employees_routes import employeesRouter
from routes.predict_ticket_routes import predictTicketRouter

app = FastAPI()

origins = [
    "http://localhost:3000",
    # Add any other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(moviesRouter, tags=["movies"], prefix="/api/v1")
app.include_router(employeesRouter, tags=["employees"], prefix="/api/v1")
app.include_router(predictTicketRouter, tags=["movies"], prefix="/api/v1")