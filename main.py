from fastapi import FastAPI, Request, File, UploadFile
import uvicorn
import pickle
import numpy as np

# Load the Random Forest Classifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello there"

@app.post("/predict")
async def predict(request: Request):
    form = await request.form()
    preg = int(form['pregnancies'])
    glucose = int(form['glucose'])
    bp = int(form['bloodpressure'])
    st = int(form['skinthickness'])
    insulin = int(form['insulin'])
    bmi = float(form['bmi'])
    dpf = float(form['dpf'])
    age = int(form['age'])
    
    data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
    my_prediction = classifier.predict(data)

    return {
        'the sample is ': my_prediction
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)


