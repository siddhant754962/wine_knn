import streamlit as st
import pandas as pd
import joblib

# ---------------- 1️⃣ Load Pipeline ----------------
knn_pipeline = joblib.load("knn_wine_pipeline.pkl")

# ---------------- 2️⃣ Load Dataset (for ranges) ----------------
df = pd.read_csv("winequality-white.csv", sep=";")
X_columns = df.drop('quality', axis=1).columns

st.title("🍷 White Wine Quality Prediction (Simple KNN)")

st.write("Enter wine features below:")

# ---------------- 3️⃣ User Input ----------------
input_features = {}
for col in X_columns:
    input_features[col] = st.number_input(
        label=col,
        min_value=float(0),
        max_value=float(100000),
        value=float(df[col].mean())
    )

input_df = pd.DataFrame([input_features])

# ---------------- 4️⃣ Predict ----------------
if st.button("Predict Quality"):
    prediction = knn_pipeline.predict(input_df)[0]
    st.subheader("Predicted Wine Quality")
    st.write(f"🍇 {prediction}")
