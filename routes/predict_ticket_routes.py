from fastapi import APIRouter
from ml_model.ml_predicted import make_predictions
from models.prediction_input_model import PredictionInput

predictTicketRouter = APIRouter()


@predictTicketRouter.post("/predict_ticket_price")
def predict(input_data: PredictionInput):
    try:
        # Extract data from the input model
        tickets_out = input_data.tickets_out
        capacity = input_data.capacity
        month = input_data.month
        day = input_data.day

        # Your existing prediction function
        predictions = make_predictions(tickets_out, capacity, month, day)

        # Return predictions as JSON
        return predictions
    except Exception as e:
        # Handle exceptions appropriately
        return {"error": str(e)}
