"""
ipyvizzu wrapper for Streamlit web-apps!
"""
from ipyvizzu import Chart, Data, Config
from typing import List
import pandas as pd
from streamlit.components.v1 import html

def bar_chart(DataFrame:pd.DataFrame,
            x: List,
            y: List,
            title: str = "",
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
    data = Data()
    data.add_data_frame(DataFrame)
    
    chart = Chart(width=width, height=height, display="manual")
    chart.animate(data)   

    chart.animate(
        Config.bar({
            "x" : x,
            "y" : y,
            "title" : title,
        })
    )
    html = chart._repr_html_()

def stacked_bubble_chart(DataFrame:pd.DataFrame,
            size: List,
            color: List,
            stackedBy: List,
            title: str = "",
            width : str = "700px", 
            height:str = "600px"
            ):
    ''' Plot Bubble chart.
    '''
    data = Data()
    data.add_data_frame(DataFrame)
    
    chart = Chart(width=width, height=height, display="manual")
    chart.animate(data)   

    chart.animate(
        Config.stackedBubble({
            "size" : size,
            "color" : color,
            "stackedBy" : stackedBy,
            "title" : title,
        })
    )
    html = chart._repr_html_()
    return html

def stacked_radial_bar(DataFrame:pd.DataFrame,
            angle: List,
            radius: List,
            stackedBy: List,
            title: str = "",
            width : str = "700px", 
            height:str = "600px"
            ):
    ''' Plot Bubble chart.
    '''
    data = Data()
    data.add_data_frame(DataFrame)
    
    chart = Chart(width=width, height=height, display="manual")
    chart.animate(data)  

    chart.animate(
        Config.radialStackedBar({
            "angle" : angle,
            "radius" : radius,
            "stackedBy" : stackedBy,
            "title" : title,
        })
    )
    return chart._repr_html_()

def vizzu_plot(HTML,
            width : int = 700,
            height : int = 600
            ):
    ''' Streamlit API to embed Vizzu HTML string 
    '''
    return html(HTML,width=width,height=height)
    