from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("artifacts/random_forest_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form (order matters!)
        features = [
            float(request.form["DRYBULBTEMPF"]),
            float(request.form["WETBULBTEMPF"]),
            float(request.form["DewPointTempF"]),
            float(request.form["RelativeHumidity"]),
            float(request.form["WindSpeed"]),
            float(request.form["WindDirection"]),
            float(request.form["StationPressure"]),
            float(request.form["SeaLevelPressure"]),
            float(request.form["Precip"])
        ]

        # Convert to array & scale
        final_features = scaler.transform([features])

        # Predict
        prediction = model.predict(final_features)[0]

        return render_template(
            "result.html",
            prediction=round(prediction, 2)
        )

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
