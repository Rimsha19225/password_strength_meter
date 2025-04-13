import streamlit as st
import random
import string

def generate_password(length, use_special_chars, use_numbers, use_uppercase, use_lowercase):
    """Generate a random password with the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Password Strength Meter")
length = st.slider("Password Length", min_value=8, max_value=32, value=12)
use_special_chars = st.checkbox("Include Special Characters")
use_numbers = st.checkbox("Include Numbers")
use_uppercase = st.checkbox("Include Uppercase Letters")
use_lowercase = st.checkbox("Include Lowercase Letters")
if st.button("Generate Password"):
    password = generate_password(length, use_special_chars, use_numbers, use_uppercase, use_lowercase)
    st.success(f"Generated Password: {password}")