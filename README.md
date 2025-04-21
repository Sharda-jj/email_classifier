# Email Classification API

This project classifies incoming emails into categories such as **REQUEST**, **PROBLEM**, or **CHANGE** etc, after detecting and masking Personally Identifiable Information (PII) such as names, phone numbers, card numbers, Aadhar, and emails.

---

## Features

- PII masking using regular expressions
- Machine learning classification using `RandomForestClassifier` in a `Pipeline`
- FastAPI backend with Dockerized deployment
- Live deployment on Hugging Face Spaces

---

## Live API (Hugging Face)

Access the live API with Swagger UI documentation:  
[https://shardaseque1206-email-classifier.hf.space/docs](https://shardaseque1206-email-classifier.hf.space/docs)

---

## Project Structure

```
email_classifier/
├── app.py                  # Uvicorn entrypoint for Hugging Face
├── api.py                  # FastAPI route for classification
├── utils.py                # PII masking function
├── models.py               # Model training script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Deployment setup for Hugging Face
├── README.md               # Project documentation
├── email_classifier.pkl    # Trained model (compressed under 100MB)
├── combined_emails_with_natural_pii.csv  # Labeled training data
└── __init__.py             # (Optional) Makes folder a Python package
```

---

## Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Sharda-jj/email_classifier.git
cd email_classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API locally

```bash
uvicorn api:app --reload
```

Visit `http://127.0.0.1:8000/docs` to interact with the API locally.

---

## Training the Model (Optional)

To retrain the model from the dataset:

```bash
python models.py
```

This reads `combined_emails_with_natural_pii.csv`, applies PII masking, and trains a classification pipeline.  
The trained model is saved to `email_classifier.pkl` using `joblib` with compression enabled.

---

## API Usage

### Endpoint: `POST /classify/`

**Request Example:**

```json
{
  "email": "Hi, I'm John Doe. My Aadhar is 1234-5678-9012. Card: 4111-1111-1111-1111"
}
```

**Response Example:**

```json
{
  "input_email_body": "...",
  "masked_email": "Hi, I'm [full_name]. My Aadhar is [aadhar_num]. Card: [credit_debit_no]",
  "list_of_masked_entities": [
    {"classification": "full_name", "entity": "John Doe"},
    {"classification": "aadhar_num", "entity": "1234-5678-9012"}
  ],
  "category_of_the_email": "Billing Issue"
}
```

---

## About `__init__.py`

The file `__init__.py` marks a directory as a Python package. While not required in modern Python (3.3+), it can be useful when organizing modular codebases or enabling relative imports.  
In this project, it is included for completeness.

---

## Submission Checklist

- [x] `app.py` (entrypoint)
- [x] `api.py` (FastAPI logic)
- [x] `models.py` (training logic)
- [x] `utils.py` (PII masking)
- [x] `requirements.txt`
- [x] `Dockerfile`
- [x] `README.md` with setup and usage instructions
- [x] Hugging Face deployment
- [x] `email_classifier.pkl` included (compressed <100MB)
- [x] `combined_emails_with_natural_pii.csv`

---

## Author

**Sharda Jadhav**  
- GitHub: [https://github.com/Sharda-jj/email_classifier](https://github.com/Sharda-jj/email_classifier)  
- Hugging Face: [https://shardaseque1206-email-classifier.hf.space](https://shardaseque1206-email-classifier.hf.space)






