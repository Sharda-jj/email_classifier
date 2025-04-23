import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib


# Load the dataset from root folder
df = pd.read_csv("combined_emails_with_natural_pii.csv")

# If masked_email column is missing, create it
if "masked_email" not in df.columns:
    from utils import mask_pii_neutral_order
    df["masked_email"] = df["email"].apply(
        lambda x: mask_pii_neutral_order(x)[0]
    )

X = df["masked_email"]
y = df["type"]

# Define model pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", RandomForestClassifier())
])

# Train the model
pipeline.fit(X, y)

# Save model
joblib.dump(pipeline, "email_classifier.pkl", compress=3)
print("Model trained and saved as email_classifier.pkl")
