import streamlit as st
import pandas as pd

# Load data
elements = pd.read_csv('input.csv')

# Define layout
table_style = """
<style>
table {
  border-collapse: collapse;
  margin: auto;
}
td {
  width: 50px;
  height: 50px;
  text-align: center;
  border: 1px solid black;
}
.button {
  background-color: #f2f2f2;
  border: 1px solid #ccc;
  color: black;
  font-size: 16px;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
"""
element_style = """
<style>
h1 {
  text-align: center;
}
img {
  display: block;
  margin: auto;
  width: 200px;
}
</style>
"""

# Display periodic table
st.markdown(table_style, unsafe_allow_html=True)
table = "<table>"
for i in range(1, 119):
    element = elements[elements['atomic_number'] == i].iloc[0]
    if element['symbol'] == '':
        table += "<tr><td colspan='2'></td></tr>"
    else:
        button = f"<a href='#' class='button' onclick=\"element_key='{element['symbol']}'\">{element['symbol']}<br>{element['name']}</a>"
        table += f"<tr><td>{button}</td><td>{element['atomic_number']}</td></tr>"
table += "</table>"
st.markdown(table, unsafe_allow_html=True)

# Display element information
st.markdown(element_style, unsafe_allow_html=True)
element_key = st.session_state.get('element_key')
if element_key:
    element = elements[elements['symbol'] == element_key].iloc[0]
    st.header(f"{element['name']} ({element['symbol']})")
    st.write(f"Atomic number: {element['atomic_number']}")
    st.write(f"Atomic mass: {element['atomic_mass']}")
    st.write(f"Period: {element['period']}")
    st.write(f"Group: {element['group']}")
    st.write(f"Electron configuration: {element['electron_configuration']}")
    st.image(f"images/{element['symbol']}.png", width=200)

