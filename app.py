from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the model and vectorizer
with open("model.pkl", "rb") as file:
    model, vectorizer = pickle.load(file)


app = FastAPI()


class Email(BaseModel):
    email_text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Email Spam Classifier API"}

@app.post("/predict")
def predict(email: Email):
    email_vectorized = vectorizer.transform([email.email_text])
    prediction = model.predict(email_vectorized)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return {"prediction": result}



