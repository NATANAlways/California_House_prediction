<<<<<<< HEAD
### California Housing Prediction

### Software and Tools Requirements


1. [Github Account](https://github.com)
2. [Heroku Account](https://heraku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


# 🏡 California House Price Prediction App

This project is a **web-based machine learning application** that predicts California house prices using multiple features (e.g., income, location, age of house). The application is built using **Flask** and a **regression model trained with scikit-learn**. Users can enter input data via a form or API and instantly get price predictions!

---

## 🚀 Features

- 🔮 Predict house prices based on input features
- 📈 Preprocessing with scaling using `StandardScaler`
- 💡 Real-time prediction via Flask web interface and REST API
- 📦 Model serialized with `pickle` (includes both scaler and regressor)
- 💻 Easily deployable with Gunicorn or any WSGI server

---

## 🧠 Machine Learning Pipeline

- **Model**: Linear Regression or other scikit-learn regressor (`regmodel.pkl`)
- **Scaler**: StandardScaler for input normalization (`scaling.pkl`)
- **Inputs** (example):
  - Median Income
  - House Age
  - Average Rooms
  - Average Bedrooms
  - Population
  - Households
  - Latitude
  - Longitude

---

## 🗂 Project Structure

```
California_House_Price/
│
├── app.py                 # Flask web server
├── regmodel.pkl           # Trained regression model
├── scaling.pkl            # StandardScaler instance
├── requirements.txt       # Dependencies
├── templates/
│   └── home.html          # Web form for user input
└── Untitled75.ipynb       # Jupyter Notebook for EDA + model training
```


## Working Sample



Create a new Environment

'''
    conda create -p venv python -y
'''

=======
# California_House_prediction
>>>>>>> bc18fe5d604f93dda8d604666ca02a9ce74c6918
