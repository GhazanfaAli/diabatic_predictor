from pydantic import BaseModel,Field
from typing import Annotated

#X_test column
"""Pregnancies	Glucose	BloodPressure	SkinThickness	
Insulin	BMI	DiabetesPedigreeFunction Age"""

#pydantic model to validate incoming data
class UserInput(BaseModel):
    Pregnancies:Annotated[int,Field(...,lt=18,desription="Number of times pregnant")]
    Glucose:Annotated[int,Field(...,lt =200,description="Plasma glucose concentration over 2 hours in an oral glucose tolerance test")]
    BloodPressure:Annotated[int,Field(...,gt =30,lt=140,description="Diastolic blood pressure (mm Hg) of the Patient")]
    SkinThickness:Annotated[int,Field(...,gt=1,lt=110,description="Triceps skinfold thickness (mm) of the Patient")]
    Insulin:Annotated[int,Field(...,lt =800,description="2-Hour serum insulin (mu U/ml) of the Patient")]
    BMI:Annotated[float,Field(...,lt=80.6,description ="Body mass index (weight in kg / height in m^2) of the Patient")]
    DiabetesPedigreeFunction:Annotated[float,Field(...,gt=0.077,lt =2.42,description="Diabetes pedigree function, a genetic score of diabetes")]
    Age:Annotated[int,Field(...,gt =20,lt=82,description ="Age of the Patient")]