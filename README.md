# Linear_Regression - Car Price Predictor

## Overview

This project implements a **Linear Regression model** to predict the price of a used car based on its key features.

The model is trained on a custom dataset and deployed through a **Flask** web application, allowing users to input car details and get an instant price prediction.

## Project Structure

```
DataScience/
│
├── Linear Regression/
│   ├── data/
│   │   └── car_price_dataset.csv
│   ├── model/
│   │   └── linear_regression_model.pkl
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── model.py
│   ├── app.py
│   └── requirements.txt
```

## Installation & Setup

1. **Clone the repository**

    ```
    git clone <your-repo-url>
    cd "DataScience/Linear Regression"
    ```

2. **Create a virtual environment (recommended)**

    ```
    python -m venv venv
    source venv/bin/activate    # For Linux/Mac
    venv\Scripts\activate       # For Windows
    ```

3. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

## Dataset

The dataset used is a custom **Car Price Dataset** with the following features:

* **Mileage** (numeric)
* **EngineSize** (numeric)
* **Age** (numeric)
* **Price** (Target: The price of the car)

## Why Linear Regression?

**Linear Regression** is a fundamental supervised learning algorithm used for predictive analysis. It models the relationship between a dependent variable (the price) and one or more independent variables (the features). This method is simple, interpretable, and effective for problems where a linear relationship between features and the target variable is assumed, making it a great starting point for price prediction tasks.

## How to Run

1. **Train the Model**

    ```
    python model.py
    ```

    This will create:

    * `linear_regression_model.pkl` (the trained model)

2. **Run the Flask App**

    ```
    python app.py
    ```

    Visit `http://127.0.0.1:5000/` in your browser.

## Prediction Goal

The application predicts the price of a car, for example: `$15,500.00`.

## Tech Stack

* **Python** – Core programming language
* **Pandas & NumPy** – Data manipulation
* **Scikit-learn** – Machine learning model training
* **Flask** – Web framework for deployment
* **HTML/CSS** – Frontend UI design

## Future Scope

* **Model Comparison:** Compare the Linear Regression model's performance against other regression algorithms like Decision Trees or Gradient Boosting.
* **Feature Engineering:** Add more features such as `make` or `model` (after proper encoding) to improve the prediction accuracy.
* **Deployment:** Deploy the Flask application to a cloud platform like Heroku or Render for public access.
* **User Interface:** Enhance the web application with a more interactive UI, providing visualizations of the data or prediction confidence.
