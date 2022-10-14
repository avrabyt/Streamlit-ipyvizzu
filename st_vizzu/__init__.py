"""
ipyvizzu wrapper for Streamlit web-apps!
"""
from ipyvizzu import Chart, Data, Config, Style
from typing import Dict, List
import pandas as pd
from streamlit.components.v1 import html
##--------------------------

class stvizzu:
    def __init__(self,x,y,title):
        self.x = x
        self.y = y
        self.title = title

        # self.width = width
        # self.height = height
    def vizzu_show(self,obj,width : int = 700,
            height : int = 600):
        _html = obj._repr_html_()
        return html(_html,width=width,height=height)     
    def vizzu_plot(self,obj,kind=""):
        pass

##---------------------------
def create_vizzu_obj(df : pd.DataFrame):
    ''' Create Vizzu Object 
    '''        
    data = Data()
    data.add_data_frame(df)
    obj = Chart(display="manual")
    obj.animate(data)
    return obj
    
def vizzu_plot(obj,
            width : int = 700,
            height : int = 600
            ):
    ''' Streamlit API to embed Vizzu object / class 
    Parameters
    -----------
    obj : ipyvizzu object/class
    width : Int
    height : Int 
    Return
    -----------
    None   
    '''
    _html = obj._repr_html_()
    return html(_html,width=width,height=height)   
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
    Return
    -------
    chart : ipyvizzu object
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
    return chart

def vizzu_animate(obj,
                config_dict : Dict = {} ,
                style_dict : Dict = {},
                ):
    ''' Animate the rendered Ipyvizzu Object.
    Parameters
    -----------
    obj : Ipyvizzu object / class
    config_dict : Dict
        Config method / argument ipyvizzu supports
    style_dict : Dict
        Styling method / arugment ipyvizzu supports
    '''
    obj.animate(
        Config(
            config_dict
        ),
        Style(
            style_dict
        ),
    )
    return obj

def beta_vizzu_animate(obj,
                x : None,
                y = None,
                size = None,
                color = None,
                label = None,
                title = None,
                geometry : str = "rectangle",
                legend = None,
                sort = "none",
                reverse = False,
                align = "none",
                split = False,
                noop = None,
                tooltip = False,
                ):
    ''' Animate the rendered Ipyvizzu Object.
    This function is deifferent from vizzu_animate as it accepts different
    ipyvizzu specific arguments without creating separate dictionaries.
    Parameters
    -----------
    obj : Ipyvizzu object / class
    x : List or Dict
        ipyvizzu channel specification. If dict use 'set' method
    y : List or Dict
        ipyvizzu channel specification
    size : List or Dict
        ipyvizzu channel specification
    color : List or Dict
        ipyvizzu channel specification
    label : List or Dict
        ipyvizzu channel specification    
    title : String
    geometry : String
        default = rectangle 
        Other options - area, line, circle
    legend : List
    sort : String 
        "byValue" or "none"
    reverse : Boolean
    align : String
        "center" "stretch"
    split : Boolean
        "True" or "False"
    noop : None
    tooltip : Boolean
        True or False

    Returns
    ------
    obj : ipyvizzu object   
    
    '''
    config_dict = {
        "channels": {
                "x": x,
                "y": y, 
                "size": size,
                "color": color,
                "label": label,               
            },
            "title": title,
            "geometry": geometry, 
            "legend": legend, 
            "sort": sort,
            "reverse": reverse,
            "align": align, 
            "split": split,
            "noop": noop,

    }
    style_dict = {}
    obj.animate(
        Config(
            config_dict
        ),
        Style(
            style_dict
        ),
    )
    if tooltip:
        obj.feature("tooltip", True)
    
    return obj

