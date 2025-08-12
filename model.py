import pandas as pd
import numpy as np
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Paths for data and model
DATA_PATH = os.path.join("dataset", "car_price_dataset.csv")
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "linear_regression_model.pkl")

# Create the model directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)

try:
    # Load the dataset
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"Error: Dataset not found at {DATA_PATH}. Please ensure the file exists.")
    exit()

# Separate features (X) and the target variable (y)
# We will use 'Mileage', 'EngineSize', and 'Age' to predict 'Price'.
# 'CarID' is an identifier and should not be used as a feature.
features = ['Mileage', 'EngineSize', 'Age']
target = 'Price'

X = df[features]
y = df[target]

# Split the data into training and testing sets
# The test size is 20% of the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model using the training data
print("Training the Linear Regression model...")
model.fit(X_train, y_train)
print("Training complete.")

# Save the trained model to a pickle file
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"Model successfully saved to {MODEL_PATH}")

