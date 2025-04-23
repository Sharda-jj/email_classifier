from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils import mask_pii_neutral_order


app = FastAPI()

# Load the saved model
model = joblib.load("email_classifier.pkl")


class EmailInput(BaseModel):
    email: str


@app.post("/classify/")
async def classify_email(email_input: EmailInput):
    raw_email = email_input.email
    masked_email, entity_list = mask_pii_neutral_order(raw_email)
    predicted_class = model.predict([masked_email])[0]

    return {
        "input_email_body": raw_email,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_email,
        "category_of_the_email": predicted_class
    }
