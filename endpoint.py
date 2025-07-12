from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.PydanticValidation import UserInput
from Schema.ResponseModel import ResponseModel
from Model.prediction import Prediction,model,model_version

app =FastAPI()
@app.get("/")
def home():
    return {"message":"Diabetic predictor"}

@app.get("/health")
def health():
    return {
        "status":"ok",
        "model_loaded": model is not None
    }

@app.post("/predtictor",response_model =ResponseModel)
def predictor(data:UserInput):
    user_input ={
        "Pregnancies":data.Pregnancies,
        "Glucose":data.Glucose,
        "BloodPressure":data.BloodPressure,
        "SkinThickness":data.SkinThickness,
        "Insulin":data.Insulin,
        "BMI":data.BMI,
        "DiabetesPedigreeFunction":data.DiabetesPedigreeFunction,
        "Age":data.Age        
    }

    try:
        prediction =Prediction(user_input)

        return JSONResponse (status_code =200,content={"response":prediction})
    except Exception as e:
        return JSONResponse (status_code =500 ,content=str(e))

