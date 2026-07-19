# 🌳 Heart Disease Prediction using Random Forest Classifier

## 📌 Project Overview

This project predicts whether a patient is likely to have **Heart Disease** using the **Random Forest Classifier** algorithm. The model is trained on the Heart Disease dataset using various medical attributes such as age, blood pressure, cholesterol, chest pain type, maximum heart rate, and more.

A user-friendly **Streamlit GUI** is developed to allow users to enter patient details and instantly predict the presence of heart disease.

---

## 🎯 Objective

To build a Machine Learning classification model that predicts Heart Disease based on patient health parameters.

---

## 📂 Dataset

**Dataset:** Heart Disease Dataset

- Total Records: ~1025
- Total Features: 13
- Target Variable: Heart Disease (0 = No Disease, 1 = Heart Disease)

### Features

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Rest ECG (restecg)
- Maximum Heart Rate (thalach)
- Exercise Induced Angina (exang)
- Oldpeak
- Slope
- Number of Major Vessels (ca)
- Thal

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## ⚙ Machine Learning Workflow

- Import Libraries
- Load Dataset
- Data Exploration
- Check Missing Values
- Feature & Target Selection
- Train-Test Split
- Train Random Forest Classifier
- Model Evaluation
- Save Model using Joblib
- Build Streamlit GUI

---

## 📊 Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🚀 Features

- Predict Heart Disease
- Interactive Streamlit Interface
- Fast Prediction
- Easy-to-use GUI
- Model Saved using Joblib

---

## 📁 Project Structure

```text
Heart-Disease-RandomForest/
│
├── app.py
├── model.pkl
├── heart.csv
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

```bash
git clone <repository-link>

cd Heart-Disease-RandomForest

pip install -r requirements.txt

streamlit run app.py
```

---

## 📸 Application

The application allows users to:

- Enter patient health details
- Click the Predict button
- Instantly know whether Heart Disease is detected or not

---

## 📈 Sample Prediction

### Input

- Age = 45
- Sex = Female
- Blood Pressure = 120
- Cholesterol = 180
- Heart Rate = 170

### Output

```
💚 No Heart Disease Detected
```

or

```
❤️ Heart Disease Detected
```

---

## 📚 Required Libraries

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib
```

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Feature Importance Graph
- Probability Prediction
- SHAP Explainability
- Model Comparison with Logistic Regression, SVM and Decision Tree

---

## 👨‍💻 Author

**Khush Arora**

B.Tech CSE Student  
Data Science Intern  
Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.