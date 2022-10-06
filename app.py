from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
import ssl
import streamlit as st 

ssl._create_default_https_context = ssl._create_unverified_context  
# Codes shamelessly adapted from here 
# - https://github.com/alod83/data-science/blob/master/DataVisualization/ipyvizzu/ipyvizzu%20Example.ipynb
st.set_page_config(page_title="Streamlit-ipyvizzu", layout="centered")
st.sidebar.title("Basic-Demo")
st.title("Streamlit :balloon: + ipyvizzu 📊")
st.sidebar.button("Animate ♻️ ")
def create_chart():
    # initialize chart
    chart = Chart(width="700px", height="600px", display="manual")
    # add data
    data = Data()
    
    data_frame = pd.read_csv('Data/eu_regions.csv',sep=';')
    data.add_data_frame(data_frame)

    chart.animate(data)

    chart.animate(
        Config({
                "channels": {
                    "y": "Country",
                    "x": ["Population (2020)","Subregion"]                    
                }
            }),
            Style({
                "plot":{"paddingLeft": "12em"}
            })
            ,y={
            "duration": 3,
            
        }
    )

    chart.animate(
        Config(
            {
                    "y": None,
                    "x": None,
                    "size": ["Country","Population (2020)"],
                    "label": "Country",
                    "color": "Subregion",
                    "geometry": "circle"
            }
        )
    )
    chart.animate(
        Config({
                "y": "Subregion",
                "x": ["Country","Population (2020)"],
                "label": None,
                "size" : None,
                "geometry": "rectangle"
            })        
    )
    
    chart.animate(
        Config({
             "x": "Population (2020)",
            "label": "Population (2020)"
            }),
        )
    

       
    return chart._repr_html_(),data_frame


CHART,df = create_chart()
html(CHART, width=700, height=600)
with st.expander(label = "Resources", expanded=False):
        st.markdown("### Data")
        st.dataframe(df)
        st.markdown('''
                    ### Code
                    [Link to original code](https://github.com/alod83/data-science/blob/master/DataVisualization/ipyvizzu/ipyvizzu%20Example.ipynb)
                    
                    [ipyvizzu](https://github.com/vizzuhq/ipyvizzu)
                    
                    ''')
        
