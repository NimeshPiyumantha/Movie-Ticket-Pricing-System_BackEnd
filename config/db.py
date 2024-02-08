from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient("mongodb+srv://root:1234@cluster0.w9benza.mongodb.net/?retryWrites=true&w=majority")

# Access the desired database
db = client["movies_ticket_pricing_db"]

collection_movies = db["movies"]
collection_employees = db["employees"]

# Ensure that the "email" field has a unique index
collection_employees.create_index("email", unique=True)