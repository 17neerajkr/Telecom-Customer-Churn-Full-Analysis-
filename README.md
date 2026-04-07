# 📊 Telecom Customer Churn Analysis & Prediction

## 🚀 Project Overview
This project focuses on analyzing and predicting customer churn in the telecom industry using **data analysis, machine learning, and business intelligence (Power BI dashboard)**.

The goal is to identify **high-risk customers**, understand **key churn drivers**, and provide **actionable insights** to improve customer retention.

---

## 🧠 Problem Statement
Customer churn is a critical problem for telecom companies as it directly impacts revenue.

This project aims to:
- Analyze customer behavior  
- Identify churn patterns  
- Predict potential churn customers  
- Support data-driven retention strategies  

---

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn)  
- **Data Analysis & EDA**  
- **Machine Learning (Random Forest)**  
- **ETL Pipeline**  
- **Power BI (Dashboard)**  
- **CI/CD (GitHub Actions)**  
- **Git & GitHub**

---

## 📁 Project Structure
Telecom-Churn/

│── data/

│── notebook/

│── src/

│   ├── data_ingestion.py

│   ├── preprocessing.py

│   ├── model_training.py

│── app.py

│── dashboard/

│   └── churn_dashboard.pbix

│── README.md




---

## 🔄 Project Workflow

### 1️⃣ Data Ingestion
- Loaded dataset using Pandas  
- Verified structure, columns, and missing values  

### 2️⃣ Data Preprocessing
- Cleaned data and handled missing values  
- Converted categorical variables into numerical format  
- Transformed target variable (**Churn: Yes/No → 1/0**)  

### 3️⃣ Exploratory Data Analysis (EDA)
- Analyzed customer distribution and churn patterns  
- Identified key features influencing churn:
  - Contract type  
  - Payment method  
  - Internet service  
  - Tenure  

### 4️⃣ Model Training
- Built a **Random Forest Classifier**  
- Split dataset into training and testing sets  
- Evaluated model performance using accuracy  

---

## ⚙️ Machine Learning Pipeline
- Data Ingestion → Preprocessing → Model Training  
- Modular code structure using Python files  
- Automated execution via `app.py`  

---

## 📊 Power BI Dashboard

### 🔝 KPI Metrics
- Total Customers: **6687**  
- Churn Customers: **1796**  
- Churn Rate: **26.86%**  

### 📈 Visualizations
- Customers by Contract Type (Donut Chart)  
- Churn by Category (Pie Chart)  
- Churn Rate by Demographics (Bar Chart)  
- Churn Rate by State (Map)  
- Interactive Filters (Gender, Contract, Payment Method)  

---

## 🔍 Key Insights
- Customers with **month-to-month contracts** have the highest churn  
- **Fiber optic users** show higher churn rates  
- **Electronic check payments** are linked to higher churn  
- Customers with **low tenure** are more likely to leave  
- **Competitor offers** are a major reason for churn  

---

## 🔗 Data Model (Relationships)
```mermaid
erDiagram

CUSTOMER {
    string CustomerID
    string Gender
    int Tenure
}

CONTRACT {
    string CustomerID
    string ContractType
}

PAYMENT {
    string CustomerID
    string PaymentMethod
    float MonthlyCharges
}

CHURN {
    string CustomerID
    int Churn
}

CUSTOMER ||--|| CONTRACT : has
CUSTOMER ||--|| PAYMENT : uses
CUSTOMER ||--|| CHURN : status


🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making

🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making

🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making

🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making

🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making

🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making

🎯 Business Impact




Helps identify high-risk customers




Supports targeted retention strategies




Improves customer lifetime value




Enables data-driven decision making
📌 Future Improvements




Add XGBoost model for better accuracy




Implement model explainability (SHAP)




Deploy using Streamlit




Integrate real-time data pipeline


