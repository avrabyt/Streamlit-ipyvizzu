from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
import ssl
import streamlit as st 

ssl._create_default_https_context = ssl._create_unverified_context  
# Codes shamelessly adapted from here 
# - https://github.com/alod83/data-science/blob/master/DataVisualization/ipyvizzu/ipyvizzu%20Example.ipynb
st.set_page_config(page_title="Streamlit-ipyvizzu", layout="centered")

st.title("Streamlit :balloon: + ipyvizzu 📊")

def create_chart():
    # initialize chart
    chart = Chart(width="700px", height="700px", display="manual")
    # add data
    data = Data()
    
    data_frame = pd.read_csv('eu_regions.csv',sep=';')
    data.add_data_frame(data_frame)

    chart.animate(data)
    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Country"]},
                    "x": {"set": ["Population (2020)"]},
                    #"color": {"set": ["Subregion"]},
                    #"y" : {"detach" : ["Subregion", "Country"]},
                    #"y": {"attach": ["Country"]},
                    
                    
                    
                    
                }
            }
        ),y={
            "duration": 3,
            #"delay": 3,
            
        }
    )



    chart.animate(
        Config(
            {
                "channels": {
                    
                    #"y" : {"detach" : {"Country"}},
                    #"y": {"attach": ["Subregion"]},
                    "x": {"set": ["Population (2020)"]},
                    "y": {"set": ["Subregion", "Country"]},
                    "color": {"set": ["Subregion"]},
                    
                    
                    
                },
                "title": "Bar Chart",
                "geometry": "rectangle",
                "orientation": "vertical",
            }
        ),
        y={
            "duration": 3,
            "delay": 3,
            
        }
    )


    chart.animate(
        Config(
            {
                "channels": {
                    #"y": {"set": ["Subregion"]},
                    "y": {"detach": ["Country"]},
                    "x": {"set": ["Population (2020)"]},
                    #"y": {"attach": ["Subregion"]},
                    "label": {"set": ["Population (2020)"]},
                
                    
                    #"size": {"set": None},
                }
            }
        )
        
    )
    chart = Chart(width="700px", height="600px", display="manual")

    chart.animate(data)

    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Country"]},
                    "x": {"set": ["Population (2020)"]},
                    
                }
            }
        ),y={
            "duration": 3,
            
        }
    )

    chart.animate(
        Config(
            {
                "channels": {
                    "y": None,
                    "x": None,
                    "size": {"set": ["Country","Population (2020)"]},
                    "label": {"set": ["Country"]},
                    "color": {"set": ["Subregion"]},
                },"geometry": "circle"
            }
        )
    )
    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Subregion"]},
                    "x": {"set": ["Population (2020)"]},
                    "y": {"set": ["Subregion"]},
                    "label": {"set": ["Population (2020)"]},
                "size" : None
                    
                    #"size": {"set": None},
                },"geometry": "rectangle"
            },
        )
        
    )
    return chart._repr_html_(),data_frame

if st.button("Rerun ♻️ "):
    pass
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
        