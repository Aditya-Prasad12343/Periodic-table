import streamlit as st
import pandas as pd

# Load periodic table data
elements = pd.read_csv("https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json")['elements']

# Define element properties to show
properties = ['name', 'symbol', 'atomic_mass', 'boiling_point', 'density', 'discovered_by']

# Create periodic table grid
table = '<table style="border-collapse: collapse; border: 1px solid black;">'
for row in range(1, 11):
    table += '<tr>'
    for col in range(1, 19):
        element = elements[(row-1)*18 + col-1]
        symbol = element['symbol']
        name = element['name']
        atomic_number = element['number']
        table += f'<td style="border: 1px solid black; padding: 5px; text-align: center;"><a href="#{symbol}">{symbol}<br>{atomic_number}</a></td>'
    table += '</tr>'
table += '</table>'

# Display periodic table
st.markdown(table, unsafe_allow_html=True)

# Create element info section
st.header("Element Info")

# Handle element click event
if st.session_state.clicked_element:
    element = elements[st.session_state.clicked_element-1]
    st.subheader(f"{element['name']} ({element['symbol']})")
    for prop in properties:
        if prop in element:
            st.write(f"{prop.capitalize()}: {element[prop]}")
else:
    st.write("Click on an element to view its information.")

# Add click event to table cells
for element in elements:
    symbol = element['symbol']
    if st.button(symbol, key=symbol):
        st.session_state.clicked_element = element['number']
