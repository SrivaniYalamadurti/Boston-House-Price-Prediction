# 🏠 Boston House Price Prediction using Machine Learning

## 📌 Project Overview

This project is a machine learning-based house price prediction application developed using Python and Scikit-learn.

The project uses housing-related features from the Boston Housing dataset to predict house prices using regression algorithms.

Two machine learning models were developed and evaluated:

- Linear Regression
- Random Forest Regression

The trained Random Forest model is integrated with a Streamlit web application, allowing users to enter housing details and receive a predicted house price.

---

## 🎯 Objective

The main objective of this project is to develop a practical machine learning system that can:

1. Load and preprocess housing data.
2. Handle missing values.
3. Separate input features and target values.
4. Train regression models.
5. Evaluate model performance.
6. Select a trained model for prediction.
7. Build an interactive web application.
8. Deploy the application for public access.

---

## 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Processing |
| Scikit-learn | Machine Learning |
| Joblib | Model Saving and Loading |
| Streamlit | Web Application |
| Git | Version Control |
| GitHub | Source Code Hosting |
| Streamlit Community Cloud | Web Deployment |

---

## 📊 Dataset

The project uses the Boston Housing dataset.

The dataset contains:

- **506 records**
- **13 input features**
- **1 target variable**

### Input Features

- CRIM – Crime rate
- ZN – Residential land zone
- INDUS – Industrial area
- CHAS – Charles River indicator
- NOX – Nitric oxide concentration
- RM – Average number of rooms
- AGE – Age of houses
- DIS – Distance to employment centers
- RAD – Highway accessibility
- TAX – Property tax rate
- PTRATIO – Pupil-teacher ratio
- B – Population-related index
- LSTAT – Lower-status population percentage

### Target

**MEDV** – Median house value.

---

## 🔄 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Checked the dataset structure.
3. Identified missing values.
4. Filled missing numerical values using median values.
5. Separated input features from the target variable.
6. Divided the dataset into training and testing sets.

### Train/Test Split

```text
Dataset
   ↓
Data Preprocessing
   ↓
Features (X) + Target (y)
   ↓
Train/Test Split
   ↓
80% Training Data
20% Testing Data

🏗️ Machine Learning Models

Two regression algorithms were implemented.

1. Linear Regression

Linear Regression was trained as a baseline regression model.

Performance:

MAE: 3.149
RMSE: 5.000
R² Score: 0.659
2. Random Forest Regression

A Random Forest Regressor was trained using multiple decision trees.

Performance:

MAE: 2.070
RMSE: 2.889
R² Score: 0.886

The Random Forest model is used in the Streamlit application.

📈 Model Evaluation

The models were evaluated using:

Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

Mean Squared Error (MSE)

Measures the average squared prediction error.

Root Mean Squared Error (RMSE)

Measures prediction error in the same scale as the target.

R² Score

Measures how much variation in the target is explained by the model.

🌐 Streamlit Web Application

A Streamlit web application was created to make the trained machine learning model easy to use.

Users can enter:

Crime rate
Residential land zone
Industrial area
Charles River indicator
Nitric oxide concentration
Average number of rooms
Age of houses
Distance to employment centers
Highway accessibility
Property tax rate
Pupil-teacher ratio
Population-related index
Lower-status population percentage

The application then predicts the house price.

Application Flow
User Enters House Details
          ↓
Input Data
          ↓
Trained Random Forest Model
          ↓
Prediction
          ↓
Predicted House Price
🖥️ Application Features
🏠 House price prediction
📊 13 housing input features
🤖 Random Forest machine learning model
⚡ Fast prediction
🌐 Web-based interface
☁️ Cloud deployment
📂 Project Structure
Boston-House-Price-Prediction/
│
├── data/
│   └── BostonHousing.csv
│
├── app.py
├── check_data.py
├── house_price_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
File Description

app.py
Contains the Streamlit web application and prediction logic.

check_data.py
Contains the data preprocessing, model training, and evaluation process.

house_price_model.pkl
Contains the trained Random Forest regression model.

BostonHousing.csv
Contains the housing dataset.

requirements.txt
Contains the Python packages required for the project.

README.md
Contains project documentation.


## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt

streamlit run app.py

http://localhost:8501

☁️ Deployment

The application will be deployed using Streamlit Community Cloud.

Deployment workflow:

GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Deploy app.py
       ↓
Public Streamlit Website

🎓 Project Information

Project: Boston House Price Prediction
Domain: Artificial Intelligence / Machine Learning
Type: Regression
Models: Linear Regression and Random Forest Regression
Dataset: Boston Housing Dataset
Interface: Streamlit
Deployment: Streamlit Community Cloud

💡 Key Learning Outcomes

Through this project, the following concepts were explored:

Machine learning fundamentals
Regression
Data preprocessing
Missing value handling
Train/test splitting
Linear Regression
Random Forest Regression
Model evaluation
MAE, MSE, RMSE and R²
Model saving using Joblib
Streamlit application development
Git and GitHub
Cloud deployment

This project demonstrates the complete workflow of a machine learning regression application, from data preprocessing and model training to model evaluation, web application development, and cloud deployment.

The project provides practical experience in building and deploying a machine learning model through an interactive web application.