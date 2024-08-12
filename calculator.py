import streamlit as st

# Function to perform basic arithmetic operations
def calculate(operation, num1, num2):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Streamlit UI - Professional Look
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>Professional Calculator</h1>", unsafe_allow_html=True)
st.markdown("### A simple and elegant calculator application built with Streamlit", unsafe_allow_html=True)

# Input fields styled with columns for better alignment
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
with col2:
    num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate and display the result
if st.button("Calculate", key="calculate_button"):
    if operation == "Division" and num2 == 0:
        st.error("Error: Division by zero is not allowed.")
    else:
        result = calculate(operation, num1, num2)
        st.success(f"**Result:** {num1} {operation.lower()} {num2} = **{result}**")

# Adding a sidebar for additional information
st.sidebar.markdown("## About This App")
st.sidebar.info(
    """
    This is a simple calculator application built using Streamlit.
    It allows you to perform basic arithmetic operations such as addition, subtraction,
    multiplication, and division with a professional and user-friendly interface.
    """
)
st.sidebar.markdown("### Developer: [Umar Majeed]")
st.sidebar.markdown("### [www.linkedin.com/in/umarmajeedofficial]")
st.sidebar.markdown("### [https://github.com/umarmajeedofficial]")
