# Real-Time-Fraud-Detection-for-POS-Lending-Platforms

### 📌 Overview
This project implements a real-time fraud detection pipeline tailored for Point-of-Sale (POS) lending platforms. It is designed to proactively identify and block fraudulent transactions occurring at merchant checkout systems, helping lending companies mitigate risk and improve customer trust.

Built using XGBoost for fraud modeling and deployed using Google Cloud Vertex AI, this system supports both real-time inference and batch scoring workflows — essential for scaling across thousands of merchant partners.

### 🧠 Business Context
Lending platforms that partner with merchants at the POS are exposed to high fraud risk due to quick, no-collateral approvals. This system enables:

Instant fraud detection at the time of transaction.

Learning from user behavior patterns over time.

Integrating fraud signals into lending decisions in real-time.

### 🔍 Project Pipeline
1. 📂 Data Ingestion
Loads transactional data, including timestamps, user/device metadata, and fraud labels.

2. 🛠️ Feature Engineering
Behavioral patterns are captured over a 7-day rolling window:

**transaction_count_7d:** High frequency of transactions in a short period may indicate account takeover or bot activity.

**avg_transaction_amount_7d:** A sudden drop or spike in average amount can signal unusual spending behavior or test transactions.

**max_transaction_amount_7d:** Detects unusually large transactions that may suggest a fraudster is trying to extract maximum value.

**total_spent_7d:** Tracks cumulative spending—suspiciously high spending in a short window can be a red flag.

**unique_merchants_7d:** A sharp increase in distinct merchants may suggest card testing or laundering through many vendors

These features help expose anomalies indicative of fraud, such as:

  High transaction velocity
  
  Sudden spikes in spend
  
  Card testing behavior

### 3. 🧼 Preprocessing
One-hot encoding for categorical variables

Scaled numeric features

Imbalance handled via scale_pos_weight in XGBoost

### 4. 🧠 Model Training
Model: XGBoostClassifier

Metrics: F1 Score, PR-AUC, ROC-AUC

Tuned to maximize recall to catch as many frauds as possible, while the threshold can be adjusted for high precision use cases

### 5. ☁️ Deployment (GCP Vertex AI)
Model deployed as a real-time endpoint

Supports live scoring and batch processing

Integrated into production for live POS decision-making

### 🖥️ Architecture

![image](https://github.com/user-attachments/assets/99b1e708-b615-45df-a823-f3b1cea74d67)

### 🔄 Real-Time Prediction
Once deployed, the system receives transaction data in real-time and returns a fraud score or binary decision (fraud/not fraud). This allows instant blocking or flagging of suspicious POS transactions.

### 🧰 Tech Stack
Python, Pandas, Scikit-learn, XGBoost

GCP Vertex AI for model deployment

DuckDB for time-based rolling features

Jupyter Notebook for development

#### 📄 Notebook Reference
Full pipeline and logic is in Real_time_fraud_detection.ipynb.

#### 🛡️ License
This project is licensed under the MIT License.
