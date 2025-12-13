import streamlit as st

# Add a title
st.title("My First Streamlit App 🚀")

# Add some text
st.write("Hello, world! This is my very first web app built with Streamlit.")

# Add an interactive widget (a slider)
age = st.slider("How old are you?", 0, 130, 25)

# Display the result of the widget interaction
st.write(f"I am {age} years old.")
