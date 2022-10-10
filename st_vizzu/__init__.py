"""
ipyvizzu wrapper for Streamlit web-apps!
"""
from ipyvizzu import Chart, Data, Config, Style
from typing import List
import pandas as pd


def bar_chart(DataFrame:pd.DataFrame,
            x: List,
            y: List,
            width : str = "700px", 
            height:str = "600px"
            ):
    ''' Plot a Bar Chart.
    Parameters
    ----------
    DataFrame : Pandas DataFrame
    x : List 
        Column name to use for the x axis
    y : List
        Column name to use for the y axis
    width : String
        Vizzu chart width
    height : String
        Vizzu chart height
    '''
    # data = pd.DataFrame()
    chart = Chart(width = width, height = height, display="manual")
    data = Data()
    data.add_data_frame(DataFrame)
    chart.animate(data)   

    # Basic Horizontal Bar
    chart.animate(
        Config(
            {
                "channels": {
                    "y": y,
                    "x": x,                   
                }
            }
        ),
    )
    return chart._repr_html_()