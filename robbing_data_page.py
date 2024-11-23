import streamlit as st
from tinydb import TinyDB

db = TinyDB("robbed_data.json")

st.set_page_config(page_title="check the json", page_icon="🧪")
st.title("check the json")
st.sidebar.header("info gets sent to json file")

name = st.text_input("Enter Full Name")
age = st.slider("Age")
country = st.text_input("Country Of Birth")

if name and age and country:
    db.insert({
        "name": name,
        "age": age,
        "country": country
    })

for name in db:
    print(name)
