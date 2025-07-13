from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Schema.PydanticValidation import UserInput
from Schema.ResponseModel import ResponseModel
from Model.prediction import Prediction, model, model_version

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Diabetic Predictor"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None
    }

@app.post("/predictor", response_model=ResponseModel)
def predictor(data: UserInput):
    user_input = {
        "Pregnancies": data.Pregnancies,
        "Glucose": data.Glucose,
        "BloodPressure": data.BloodPressure,
        "SkinThickness": data.SkinThickness,
        "Insulin": data.Insulin,
        "BMI": data.BMI,
        "DiabetesPedigreeFunction": data.DiabetesPedigreeFunction,
        "Age": data.Age
    }

    try:
        prediction = Prediction(user_input)
        return JSONResponse(status_code=200, content={"response": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Internal server error"})