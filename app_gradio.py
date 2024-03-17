import gradio as gr
import requests

def make_prediction(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age):
    url = 'http://localhost:8000/predict'
    data = {
        'pregnancies': pregnancies,
        'glucose': glucose,
        'bloodpressure': bloodpressure,
        'skinthickness': skinthickness,
        'insulin': insulin,
        'bmi': bmi,
        'dpf': dpf,
        'age': age
    }

    response = requests.post(url, data=data)
    result = response.json()
    prediction = result['the sample is ']
    return prediction

inputs = [
    gr.inputs.Number(label="Pregnancies"),
    gr.inputs.Number(label="Glucose"),
    gr.inputs.Number(label="Blood Pressure"),
    gr.inputs.Number(label="Skin Thickness"),
    gr.inputs.Number(label="Insulin"),
    gr.inputs.Number(label="BMI"),
    gr.inputs.Number(label="Diabetes Pedigree Function"),
    gr.inputs.Number(label="Age")
]

output = gr.outputs.Textbox(label="Prediction")

title = "Diabetes Prediction"
description = "Enter the patient's information to predict the likelihood of diabetes."

iface = gr.Interface(fn=make_prediction, inputs=inputs, outputs=output, title=title, description=description)

if __name__ == "__main__":
    iface.launch(share = True)