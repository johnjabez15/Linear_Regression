from flask import Flask, render_template, request
import os
import pickle
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Define the paths for the model and other directories
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "linear_regression_model.pkl")

# Load the trained model pipeline
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    print(f"Error: The model file was not found at {MODEL_PATH}.")
    print("Please run model.py first to train and save the model.")
    exit()

@app.route('/')
def home():
    """Renders the home page with the car price prediction form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles the prediction request from the form.
    
    It collects the user's input, converts it into a pandas DataFrame,
    and then uses the loaded Linear Regression model to make a prediction.
    The predicted price is then displayed on a result page.
    """
    try:
        # Get the form data from the POST request
        mileage = float(request.form['Mileage'])
        engine_size = float(request.form['EngineSize'])
        age = int(request.form['Age'])
        
        # Create a pandas DataFrame from the input, ensuring column order matches the model's training data
        input_data = pd.DataFrame([[mileage, engine_size, age]], 
                                  columns=['Mileage', 'EngineSize', 'Age'])

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]

        # Format the prediction as a currency string for better display
        formatted_prediction = f"${prediction:,.2f}"

        # Render the result page with the prediction
        return render_template('result.html', prediction=formatted_prediction)

    except ValueError:
        # Handle cases where the input is not a valid number
        error_message = "Invalid input. Please enter valid numbers for all fields."
        return render_template('result.html', prediction=error_message)
    except Exception as e:
        # Handle any other unexpected errors
        error_message = f"An error occurred: {str(e)}"
        return render_template('result.html', prediction=error_message)

if __name__ == '__main__':
    # Run the app. It will be accessible at http://127.0.0.1:5000/
    app.run(debug=True)
