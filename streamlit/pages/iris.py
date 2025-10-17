import streamlit as st
import pickle

# Load the model
model = pickle.load(open("model/iris_model.pkl", "rb"))

# Custom CSS for beautification
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🌸 Iris Species Predictor")
st.subheader("Predict the species of an Iris flower using its dimensions")

st.markdown("### 🌿 Please enter the flower measurements below:")

with st.form("iris_form"):
    col1, col2 = st.columns(2)

    with col1:
        sl = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1, format="%.1f")
        sw = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1, format="%.1f")

    with col2:
        pl = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1, format="%.1f")
        pw = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1, format="%.1f")

    submitted = st.form_submit_button("🌼 Predict")

# Prediction Logic
if submitted:
    features = [[sl, sw, pl, pw]]
    prediction = model.predict(features)
    species = prediction[0]
    
    st.markdown("---")
    st.success(f"🎉 The predicted Iris species is: **{species}**")
    st.markdown("🌱 Thank you for using the Iris predictor!")
