import streamlit as st
import requests
import os
from bs4 import BeautifulSoup

ios.environ["HUGGINGFACEHUB_API_TOKEN"] = "--=--"

# Function to fetch player stats
def fetch_player_stats(player_name):
    """Fetches cricket stats for a given player name"""
    url = f"https://api.cricapi.com/v1/players?name={player_name}&apikey=YOUR_API_KEY"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("response", "No data available for this player.")
    except Exception as e:
        return f"Error fetching data: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="CricBot - Cricket AI", layout="centered")

# Title & Subtitle
st.image("b42ff828da8080b3e4e9d88a58c33b9f.png", width=90)
st.title("CricBot 🏏")
st.subheader("Ask Anything About Cricket!")

# Chat Interface
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message("user" if msg["is_user"] else "assistant"):
        st.write(msg["text"])

# User Input
query = st.text_input("Ask your Cricket Query", key="querybox")
if st.button("Submit"):
    if query:
        # Display User Query
        st.session_state.chat_history.append({"text": query, "is_user": True})
        with st.chat_message("user"):
            st.write(query)

        # Fetch and Display Response
        response = fetch_player_stats(query)
        st.session_state.chat_history.append({"text": response, "is_user": False})
        with st.chat_message("assistant"):
            st.write(response)

st.write("\n\n---\nCricBot by Team MnC 🏏")
