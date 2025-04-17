from google.cloud import aiplatform
import pandas as pd

# Initialize the client
aiplatform.init(project="your-gcp-project", location="us-central1")

# Sample transaction input (replace with actual input format used during training)
sample_data = {
    "transaction_amount": 120.5,
    "transaction_hour": 14,
    "credit_score": 690,
    "account_age_days": 430,
    "user_has_2fa_enabled": 1,
    "user_has_fraudulent_transactions_7d": 0,
    "declined_transaction_count_3d": 1,
    "failed_login_attempts_24h": 0,
    "device_count_30d": 2,
    "country_count_7d": 1,
    "email_verified": 1,
    "kyc_verified": 1,
    "velocity_within_session": 2,
    "card_present": 1,
    "is_first_transaction": 0,
    "transaction_count_7d": 4,
    "avg_transaction_amount_7d": 80.0,
    "max_transaction_amount_7d": 150.0,
    "unique_merchants_7d": 3,
    "total_spent_7d": 320.0,
    "transaction_type": "pos",
    "channel": "mobile",
    "location": "urban"
}

# Convert to the format your endpoint expects (list of instances)
instances = [sample_data]

# Send to Vertex AI endpoint
endpoint = aiplatform.Endpoint(endpoint_name="projects/your-project/locations/us-central1/endpoints/your-endpoint-id")
response = endpoint.predict(instances=instances)

print("Prediction:", response.predictions)
