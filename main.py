import streamlit as st
import pandas as pd

# Load the periodic table data
df = pd.read_csv('input.json')['elements']
elements = {d['symbol']: d for d in df.to_dict('records')}

# Define the HTML template for the tooltip
html_template = """
<div style="background-color: #F4F4F4; padding: 10px;">
    <h4 style="margin-top: 0px;">{name} ({symbol})</h4>
    <p><b>Atomic number:</b> {number}</p>
    <p><b>Atomic mass:</b> {atomic_mass}</p>
    <p><b>Category:</b> {category}</p>
    <p><b>Electron configuration:</b> {electron_configuration}</p>
</div>
"""

# Define the CSS style for the tooltip
css_style = """
<style>
    /* Tooltip container */
    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
    }

    /* Tooltip text */
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #F4F4F4;
        color: black;
        text-align: center;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    /* Tooltip text arrow */
    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: black transparent transparent transparent;
    }

    /* Show the tooltip text when you mouse over the tooltip container */
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
</style>
"""

# Display the periodic table
st.markdown(css_style, unsafe_allow_html=True)
for row in range(1, 10):
    for col in range(1, 19):
        symbol = f'{col+((row-1)*18):03}'
        element = elements.get(symbol, {})
        if element:
            tooltip_html = html_template.format(**element)
            html = f'<div class="tooltip">{element["symbol"]}<span class="tooltiptext">{tooltip_html}</span></div>'
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write('')

