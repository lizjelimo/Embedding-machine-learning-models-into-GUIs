import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set a predefined username and password from environment variables
USERNAME = os.getenv("STREAMLIT_USERNAME")
PASSWORD = os.getenv("STREAMLIT_PASSWORD")

# Function to display the login form
def show_login():
    st.title("Login")

    # Check if the user is already authenticated
    if st.session_state.get('authenticated', False):
        st.success(f"Welcome back, {st.session_state['username']}!")
        return True

    # Create a form for username and password input
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    # Check the credentials
    if login_button:
        if username == USERNAME and password == PASSWORD:
            st.success("Login successful!")
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
            return True
        else:
            st.error("Invalid username or password. Please try again.")
            return False

    # If not authenticated, display a message
    st.warning("Please log in to continue.")
    return False


if __name__ == "__main__":
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if show_login():
        st.write("You are logged in! Access your app content here.")
    else:
        st.write("Login to access the app.")

