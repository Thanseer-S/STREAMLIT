import streamlit as st
import pickle 

model = pickle.load(open("model/iris_model.pkl", "rb"))


st.title("New app iris")
st.header("Enter details")

#st.text_input("Enter the sepal length")
#st.text_input("Enter the petal length")
#st.text_input("Enter the sepal width")
#st.text_input("Enter the petal width")
#st.button('predict')


with st.form("iris_app_form"):
    sl = st.text_input("Enter sepal length")
    pl = st.text_input("Enter petal length")
    sw = st.text_input("Enter sepal width")
    pw = st.text_input("Enter petal width")

    submitted = st.form_submit_button("predict species")

if submitted:
    prediction = model.predict([[sl, pl, sw, pw]])
    st.success(f"predicted spicies {prediction}")
