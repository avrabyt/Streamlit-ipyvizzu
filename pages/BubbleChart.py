import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
from streamlit.components.v1 import html
import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer 

def BubbleChart(df:pd.DataFrame):
    ''' Create BubbleChart
    Parameters
    -----------
    data_frame : DataFrame
        The data to display.
    
    Returns
    -----------
    HTML String
    '''
    # Initialize <class 'ipyvizzu.animation.Data'>
    data = Data()
    data.add_data_frame(df)
    # A class for representing a wrapper over Vizzu chart. <class 'ipyvizzu.chart.Chart'>
    chart = Chart(display="manual")
    # A method for animating the chart.
    chart.animate(data)
    chart.animate(
        Config(
            {
                "channels": {
                    "color": {"set": ["Joy factors"]},
                    "size": {"set": ["Value 2 (+)"]},
                    "label": {"set": ["Country_code"]},
                },
                "title": "Bubble Chart",
                "geometry": "circle",
            }
        )
    )
    features = [ "Value 2 (+)","Country_code"]
    chart.animate(
        Config(
            {
                "channels": {
                    "size": {"set": features}
                    },
                    "title": "Stacked Bubble Chart",
            }
        ),
        Style({"plot": {"marker": {"label": {"fontSize": 10}}}}),
    )
    return chart._repr_html_()

@st.cache_data
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
    return pd.read_csv(data_path, dtype={"Year": str, "Timeseries": str})

# ------ App ----------
# st.set_page_config(page_title="Streamlit-ipyvizzu", layout="centered")
st.sidebar.title("Bubble Chart-Demo")
data_path = "Data/chart_types_eu.csv"
df = load_data(data_path=data_path)

with st.sidebar:
    filtered_df = dataframe_explorer(df)
with st.expander("DataFrame ⤵️"):
    st.dataframe(filtered_df)
_CHART = BubbleChart(filtered_df)
html(_CHART, width=700, height=600)
st.sidebar.button("Animate ♻️", type='primary')
