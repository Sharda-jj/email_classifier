---
title: Email Classifier API
emoji: 📬
colorFrom: yellow
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
---

# 📧 Email Classification API

This project classifies incoming emails into categories like **Billing Issue**, **Technical Support**, etc., after masking sensitive Personally Identifiable Information (PII) such as names, phone numbers, Aadhar, and card details.

It uses:
- ✅ Regex-based PII masking
- ✅ A trained `RandomForestClassifier` inside a `Pipeline`
- ✅ FastAPI to serve the classification API
- ✅ Docker-based deployment on Hugging Face Spaces

---

## 🔗 Live API (Hugging Face)

**Test it here:**  
👉 https://shardaseque1206-email-classifier.hf.space/docs  
(Swagger UI to interact with the `/classify/` endpoint)

---

## 📂 Project Structure

```
email-classifier/
├── app.py                # Uvicorn entrypoint
├── api.py                # FastAPI logic (routes + classification)
├── utils.py              # PII masking logic
├── models.py             # Model training script
├── requirements.txt      # Python dependencies
├── email_classifier.pkl  # Trained ML model
├── Dockerfile            # For Hugging Face Spaces deployment
└── README.md             # This file
```

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run API locally

```bash
uvicorn api:app --reload
```

### 3. Train model (optional)

```bash
python models.py
```

---

## 🧪 API Usage

### Endpoint: `POST /classify/`

**Request:**

```json
{
  "email": "Hi, I'm John Doe. My Aadhar is 1234-5678-9012. Card: 4111-1111-1111-1111"
}
```

**Response:**

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

## ✅ Submission Requirements

- [x] `app.py` main script
- [x] `requirements.txt`
- [x] `README.md` with setup and usage
- [x] `models.py` to train the classifier
- [x] `utils.py` for masking logic
- [x] `api.py` for FastAPI
- [x] Deployed on Hugging Face + deployment link provided

---

## 🧠 Author

**Sharda Jadhav**  
Deployment: https://shardaseque1206-email-classifier.hf.space
