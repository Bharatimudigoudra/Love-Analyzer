import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://bharatimudigoudra912000:912000@cluster0.no155.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# create a database 
db = client['Love']
# In mongodb data collection 
collection = db["Love_cal"]

# Function to calculate True Love Percentage
def love_calculator(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    combined_names = name1 + name2
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")

    love_score = int(str(true_count) + str(love_count)) % 101  # Ensuring percentage stays within 0-100
    return love_score

# Function for FLAMES Game Relationship Calculation
def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    count = len(name1 + name2)
    flames = ["F", "L", "A", "M", "E", "S"]

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index+1:] + flames[:split_index]
        else:
            flames.pop()

    result_map = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    return result_map[flames[0]]

# Streamlit App UI
st.title("💖 True Love & Relationship Calculator 💖")
st.write("Find out your relationship type and love percentage!")

# User Input
name1 = st.text_input("Enter your name:")
name2 = st.text_input("Enter their name:")

if st.button("Calculate"):
    if name1 and name2:
        # Compute results
        relationship = flames_game(name1, name2)
        love_percentage = love_calculator(name1, name2)

        # Display results
        st.subheader("🔮 Relationship Result:")
        st.success(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: **{relationship}!** 💞")

        st.subheader("❤️ True Love Percentage:")
        st.info(f"Your True Love Score is **{love_percentage}%** 💖")

    else:
        st.warning("Please enter both names to calculate!")

