from st_vizzu import *
import pandas as pd
import ssl
import streamlit as st 
# from page_config import standard_page_widgets
from streamlit_extras.mention import mention
# Add this on top of any page to make mpa-config work!
# standard_page_widgets()

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
# App
# st.set_page_config(page_title="Streamlit-ipyvizzu", layout="centered")
st.sidebar.title("Basic-Demo")
st.sidebar.button("Animate ♻️ ")

# Load Data
file_path = 'Data/eu_regions.csv'
df = pd.read_csv(file_path,sep=';')

# Create ipyvizzu Object
obj = create_vizzu_obj(df)
config_dict = {"channels": {"y": ["Country"],"x": ["Population (2020)","Subregion"] }}
style_dict = {"plot":{"paddingLeft": "12em"}}
# Animate with general dict based arguments 
anim_obj = vizzu_animate(obj,config_dict=config_dict,style_dict=style_dict)
# Animate with argument based
anim_obj1 = beta_vizzu_animate(anim_obj,
    x=None,y=None,size=["Country","Population (2020)"],
    label="Country", color="Subregion",geometry="circle")
# Will use beta vizzu animate when Style reinitializing issue resolved
anim_obj2 = vizzu_animate(anim_obj1,
                {
                "y": "Subregion",
                "x": ["Country","Population (2020)"],
                "label": None,
                "size" : None,
                "geometry": "rectangle"
            }
    
        )
anim_obj3 = vizzu_animate(anim_obj2,
            config_dict={
            "x": "Population (2020)",
            "label": "Population (2020)"
            })
with st.container():
    vizzu_plot(anim_obj3,width=800,height=800)

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

