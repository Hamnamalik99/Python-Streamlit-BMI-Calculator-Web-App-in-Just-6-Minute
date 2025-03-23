

import streamlit as st

# Custom CSS for light theme
st.markdown(
    """
    <style>
        body {
            background-color: #f7f7f7;
            color: #333;
        }
        .stApp {
            background-color: #f7f7f7;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 8px 16px;
            border-radius: 8px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stNumberInput>div>input {
            font-size: 14px;
            padding: 8px;
            border-radius: 6px;
            border: 1px solid #ddd;
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            background: white;
            color: black;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            margin: 20px auto;
            max-width: 400px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown("<h1 style='text-align: center; color: #333;'>💪 BMI Calculator</h1>", unsafe_allow_html=True)

# Centered container for inputs
st.markdown("<div class='card'>", unsafe_allow_html=True)

# Input fields for weight and height
weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("📏 Enter your height (m)", min_value=0.1, step=0.01)

st.markdown("</div>", unsafe_allow_html=True)

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.markdown(f"<h2 style='text-align: center; color: #444;'>📊 Your BMI is: **{bmi:.2f}**</h2>", unsafe_allow_html=True)

        # BMI Category
        if bmi < 18.5:
            st.warning("⚠️ You are **Underweight**. Consider a healthy diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a **Normal Weight**. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **Overweight**. Try to stay active.")
        else:
            st.error("❌ You are **Obese**. Consider a healthier lifestyle.")
    else:
        st.error("⚠️ Height must be greater than zero.")