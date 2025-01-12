# Email Spam Classification using Machine Learning

## Project Overview

This project is a simple **Email Spam Classification** application built using **Machine Learning** and **FastAPI**. The model classifies emails as either **spam** or **not spam** based on the content of the email. It uses a machine learning model trained on a dataset of labeled emails and exposes a FastAPI-based REST API for making predictions.

The project includes:
- **Training a machine learning model** using a labeled email dataset.
- **Building a FastAPI** backend that serves the model and allows users to make predictions via an HTTP API.
- The model is saved in the **model.pkl** file for reuse in the API.

## Files in the Repository

1. **`app.py`**  
   - A FastAPI application that exposes an endpoint (`/predict`) to predict whether an email is spam or not. The model is loaded from the `model.pkl` file, and predictions are made based on the email text provided.

2. **`mail_data.csv`**  
   - The training dataset used to build the machine learning model. It contains labeled email content, where the `text` column holds the email content, and the `label` column has the value `1` for spam and `0` for not spam.

3. **`model.pkl`**  
   - The trained machine learning model serialized using **Pickle**. It contains the trained classifier and vectorizer for transforming email text into a format suitable for the model.

4. **`requirements.txt`**  
   - A list of Python packages required to run the project, including FastAPI, Uvicorn, and scikit-learn.

5. **`test.csv`**  
   - A test dataset used to evaluate the model's performance on unseen data. It contains email content and corresponding labels (spam or not).
