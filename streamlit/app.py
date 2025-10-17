import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="🌟 Streamlit UI with Image & Colors",
    layout="centered"
)

# Custom background and styling
st.markdown("""
    <style>
        body {
            background-image: linear-gradient(to top left, #ffecd2 0%, #fcb69f 100%);
            background-attachment: fixed;
            background-size: cover;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #c40000;
        }
        h1, h2, h3 {
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Display a banner image (can use any URL or upload your own)
st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", 
         caption="🌸 Beautiful Nature - Welcome!", use_column_width=True)

# Main content
st.title("🌟 Streamlit App with Image & Colorful Background")
st.header("🎨 Interactive, Stylish Web App")
st.subheader("🔧 Powered by Streamlit + Python")

# User inputs
name = st.text_input("👤 Enter your name", placeholder="e.g., Alice")
age = st.slider("🎂 Select your age", 10, 60, 25)
contact = st.selectbox("📞 Preferred Contact Method", ["Email", "Phone", "SMS"])

# Show a data table
st.markdown("### 🌡️ Sample City Temperature Data")
data = pd.DataFrame({
    "🏙️ City": ["Kochi", "Chennai", "Bangalore"],
    "🌡️ Temperature (°C)": [30, 40, 35]
})
st.dataframe(data, use_container_width=True)

# Image section (local or URL)
st.markdown("### 🖼️ Sample Iris Flower Image")
st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", 
         caption="Iris Flower Example", width=400)

# Feedback display
if name:
    st.markdown("---")
    st.success(f"""
    ✅ Hello, **{name}**!  
    🎉 You are **{age}** years old and prefer **{contact}** as your contact method.  
    🌟 Thanks for using this beautiful Streamlit app!
    """)

# Footer
st.markdown("---")
st.markdown("🧡 _Created with Streamlit by You_")
