import streamlit as st
import json

# Load the data
with open("https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json") as f:
    data = json.load(f)
    elements = data["elements"]

# Define the columns to show
columns = ["name", "symbol", "atomic_mass", "category", "appearance", "boil", "melt", "density", "discovered_by"]

# Define the app layout
st.set_page_config(page_title="Periodic Table", page_icon=":atom_symbol:", layout="wide")
st.title("Periodic Table")

# Create a grid of buttons to display the elements
col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
for i in range(len(elements)):
    element = elements[i]
    button = None
    if element["category"] == "diatomic nonmetal":
        button = col1.button(element["symbol"], key=i)
    elif element["category"] == "noble gas":
        button = col2.button(element["symbol"], key=i)
    elif element["category"] == "alkali metal":
        button = col3.button(element["symbol"], key=i)
    elif element["category"] == "alkaline earth metal":
        button = col4.button(element["symbol"], key=i)
    elif element["category"] == "metalloid":
        button = col5.button(element["symbol"], key=i)
    elif element["category"] == "halogen":
        button = col6.button(element["symbol"], key=i)
    else:
        button = col7.button(element["symbol"], key=i)

    # Display the element information when button is clicked
    if button:
        st.write("## " + element["name"])
        for col in columns:
            if col in element:
                st.write("**" + col.capitalize().replace("_", " ") + ":**", element[col])
