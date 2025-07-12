import pandas as pd
import pickle

# Load model dynamically (Vercel sets the working directory to /var/task)
with open("/var/task/Model/Diabets_Models.pkl", "rb") as f:
    model = pickle.load(f)

model_version = "1.0.0"

def Prediction(user_input: dict):
    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    return output