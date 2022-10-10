from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
import ssl
import streamlit as st 
from page_config import standard_page_widgets
from streamlit_extras.mention import mention
# Add this on top of any page to make mpa-config work!
standard_page_widgets()
@st.experimental_memo()
def load_data(data_path:str):
    ''' Load the data
    Parameter
    ---------
    data_path : String 
        Path to Data File
    Returns
    -------
        Pandas.DataFrame
    ''' 
    return pd.read_csv(data_path,sep=';')

ssl._create_default_https_context = ssl._create_unverified_context  
# Codes adapted from here 
# - https://github.com/alod83/data-science/blob/master/DataVisualization/ipyvizzu/ipyvizzu%20Example.ipynb

def create_chart(df):
    # initialize chart
    chart = Chart(width="700px", height="600px", display="manual")
    # add data
    data = Data()
    
    data.add_data_frame(df)
    
    chart.animate(data)   
    Y = ["Country"]
    X = ["Population (2020)","Subregion"] 
    # Basic Horizontal Bar
    chart.animate(
        Config(
            {
                "channels": {
                    "y": Y,
                    "x": X,                   
                }
            }
            ),
            Style(
                {
                "plot":{"paddingLeft": "12em"}
            }
            ),
            y = {
                "duration": 3,   
        }
    )
    
    chart.animate(
        Config(
            {
                    "y": None,
                    "x": None,
                    "size": ["Country","Population (2020)"],
                    # "size": ["Population (2020)"],
                    "label": "Country",
                    "color": "Subregion",
                    "geometry": "circle"
            }
        )
    )
    chart.animate(
        Config(
            {
                "y": "Subregion",
                "x": ["Country","Population (2020)"],
                "label": None,
                "size" : None,
                "geometry": "rectangle"
            }
            )        
    ) 
    chart.animate(
        Config(
            {
            "x": "Population (2020)",
            "label": "Population (2020)"
            }
            ),
        )
    return chart._repr_html_()

# App
# st.set_page_config(page_title="Streamlit-ipyvizzu", layout="centered")
st.sidebar.title("Basic-Demo")
st.sidebar.button("Animate ♻️ ")

# Load Data
file_path = 'Data/eu_regions.csv'
df = pd.read_csv(file_path,sep=';')
# st.dataframe(df)
CHART = create_chart(df)
html(CHART, width=700, height=600)

with st.sidebar:
    mention(
        label="Resources",
        icon="github",  # Some icons are available... like Streamlit!
        url="https://github.com/alod83/data-science/blob/master/DataVisualization/ipyvizzu/ipyvizzu%20Example.ipynb",
    )

    mention(
        label="ipyvizzu-repositiory",
        icon="github",  # Some icons are available... like Streamlit!
        url="https://github.com/vizzuhq/ipyvizzu",
    )
# from streamlit_extras.app_logo import add_logo
# add_logo("https://vizzuhq.com/images/icons/ipyvizzu_button.png")
