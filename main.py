import streamlit as st
import json

# Load the data
with open("input.json", "r") as file:
    data = json.load(file)
    elements = data["elements"]

# Define the columns to show
columns = ["name", "symbol", "atomic_mass", "category", "appearance", "boil", "melt", "density", "discovered_by"]

# Define the app layout
st.set_page_config(page_title="Periodic Table", page_icon=":atom_symbol:", layout="wide")
st.title("Periodic Table")

# Create a grid of buttons to display the elements
cols = st.columns(7)
for i in range(len(elements)):
    element = elements[i]
    button = None
    if element["category"] == "diatomic nonmetal":
        button = cols[0].button(element["symbol"], key=i)
    elif element["category"] == "noble gas":
        button = cols[1].button(element["symbol"], key=i)
    elif element["category"] == "alkali metal":
        button = cols[2].button(element["symbol"], key=i)
    elif element["category"] == "alkaline earth metal":
        button = cols[3].button(element["symbol"], key=i)
    elif element["category"] == "metalloid":
        button = cols[4].button(element["symbol"], key=i)
    elif element["category"] == "halogen":
        button = cols[5].button(element["symbol"], key=i)
    else:
        button = cols[6].button(element["symbol"], key=i)

    # Display the element information when button is clicked
    if button:
        st.write("## " + element["name"])
        for col in columns:
            if col in element:
                st.write("**" + col.capitalize().replace("_", " ") + ":**", element[col])
