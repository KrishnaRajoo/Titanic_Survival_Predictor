import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# -------------------------
# Data Preprocessing
# -------------------------

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df.drop("Cabin", axis=1, inplace=True)

df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

df["Embarked"] = df["Embarked"].map({
    "S": 0,
    "C": 1,
    "Q": 2
})

df.drop(
    ["PassengerId", "Name", "Ticket"],
    axis=1,
    inplace=True
)

# -------------------------
# Features
# -------------------------

X = df.drop("Survived", axis=1)
y = df["Survived"]

# -------------------------
# Train Model
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# -------------------------
# Save Model
# -------------------------

joblib.dump(model, "titanic_model.pkl")

print("✅ Model trained and saved successfully!")