import joblib

# Load the model from best_model.joblib
loaded_model = joblib.load('best_model.joblib')

# Print the contents of the loaded model
print("Model Parameters:")
print(loaded_model)

# Optionally, you can print specific attributes of the model if available
# For example, if the model has a 'coef_' attribute (for linear models), you can print it
if hasattr(loaded_model, 'coef_'):
    print("Model Coefficients:")
    print(loaded_model.coef_)

# Add more print statements or attribute access as needed based on your model type
