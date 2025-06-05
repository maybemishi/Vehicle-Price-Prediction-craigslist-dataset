# Vehicle-Price-Prediction-craigslist-dataset

This project builds a regression model to predict used vehicle prices based on a wide range of features like manufacturer, model, fuel type, year, mileage, and more. The goal is to demonstrate data preprocessing, feature engineering, and model training using **LightGBM** in a real-world context.


## 📌 Project Objectives

- Clean and preprocess a large real-world dataset
- Handle missing values intelligently using various strategies
- Encode categorical variables using `OneHotEncoder`
- Build and evaluate a regression model with LightGBM
- Interpret performance with RMSE and R² score


## 📂 Dataset

The dataset used for this project is publicly available on Kaggle:  
🔗 **[Used Cars Dataset - Craigslist](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)**


## 🧠 Tools & Libraries

- **Languages & Frameworks**: Python, Jupyter Notebook  
- **Libraries**:  
  - `pandas`, `numpy` – data handling  
  - `scikit-learn` – preprocessing and evaluation  
  - `lightgbm` – model training  


## 📈 Model Performance

- **R² Score**: `0.8008`  
- **Test RMSE**: `6434.15`

✅ This means the model can explain around **80%** of the variance in vehicle prices—strong for such a diverse dataset.
