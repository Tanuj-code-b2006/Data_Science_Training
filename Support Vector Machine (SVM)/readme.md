# ❤️ Heart Disease Prediction using Support Vector Machine (SVM)

## 📌 Project Overview

This project predicts whether a patient is likely to have **Heart Disease** using the **Support Vector Machine (SVM)** classification algorithm. The model is trained on the Heart Disease dataset using various medical parameters such as age, blood pressure, cholesterol, chest pain type, heart rate, and more.

A simple and interactive **Streamlit GUI** is developed for real-time prediction.

---

## 🎯 Objective

To build a Machine Learning classification model using **Support Vector Machine (SVM)** for predicting Heart Disease.

---

## 📂 Dataset

**Dataset:** Heart Disease Dataset

- Total Records: ~1025
- Total Features: 13
- Target Variable:
  - 0 → No Heart Disease
  - 1 → Heart Disease

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
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## ⚙ Machine Learning Workflow

- Import Libraries
- Load Dataset
- Data Exploration
- Check Missing Values
- Feature Selection
- Train-Test Split
- Feature Scaling (StandardScaler)
- Train SVM Classifier
- Model Evaluation
- Save Model using Joblib
- Build Streamlit GUI

---

## 🤖 Machine Learning Algorithm

- Support Vector Machine (SVM)

---

## 📊 Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🚀 Features

- Heart Disease Prediction
- Fast Prediction
- Interactive Streamlit GUI
- Easy User Interface
- Machine Learning Deployment Ready

---

## 📁 Project Structure

```text
Heart-Disease-SVM/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── heart.csv
├── Heart_Disease_SVM.ipynb
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

```bash
git clone <repository-link>

cd Heart-Disease-SVM

pip install -r requirements.txt

streamlit run app.py
```

---

## 📸 Application

The application allows users to:

- Enter patient health information
- Predict Heart Disease
- Display prediction instantly

---

## 📈 Sample Prediction

### Input

- Age = 45
- Sex = Female
- Blood Pressure = 120
- Cholesterol = 180
- Maximum Heart Rate = 170

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

- Hyperparameter Tuning using GridSearchCV
- Probability Prediction
- Feature Importance Analysis
- SHAP Explainability
- Compare with Logistic Regression, Decision Tree and Random Forest

---

## 👨‍💻 Author

**Khush Arora**

B.Tech CSE Student  
Data Science Intern  
Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.