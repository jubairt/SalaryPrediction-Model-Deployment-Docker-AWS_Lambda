import json
import joblib
import numpy as np

model = joblib.load("model.pkl")

def lambda_handler(event, context):
    # If coming from API Gateway, data is in event["body"]
    if "body" in event and event["body"]:
        data = json.loads(event["body"])
    else:
        # Direct Lambda test
        data = event

    years_exp = data.get("years_experience")

    if years_exp is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "years_experience is required"})
        }

    input_data = np.array([[float(years_exp)]])
    prediction = model.predict(input_data)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "years_experience": years_exp,
            "predicted_salary": float(prediction[0])
        })
    }
