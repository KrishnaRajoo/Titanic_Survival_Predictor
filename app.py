from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("titanic_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    pclass = int(request.form["Pclass"])
    sex = int(request.form["Sex"])
    age = float(request.form["Age"])
    sibsp = int(request.form["SibSp"])
    parch = int(request.form["Parch"])
    fare = float(request.form["Fare"])
    embarked = int(request.form["Embarked"])

    # Create dataframe
    data = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked]
    })

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)

    confidence = round(max(probability[0]) * 100, 2)

    if prediction == 1:
        result = "🟢 Passenger is likely to Survive"
    else:
        result = "🔴 Passenger is unlikely to Survive"

    return render_template(
        "index.html",
        prediction_text=result,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)