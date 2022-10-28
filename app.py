from st_vizzu import *
import pandas as pd
import streamlit as st
# works with streamlit version streamlit==1.13.0
from page_config import standard_page_widgets
# Add this on top of any page to make mpa-config work!
standard_page_widgets()

st.markdown(''' 
            ### Create animated charts easily! 
            A [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) wrapper for intuitive usage of ipyvizzu functions and Streamlit embed support. 
            
            ''')
# Load Data
df = pd.read_csv("Data/music_data.csv", index_col=0)
# Create ipyvizzu Object
obj = create_vizzu_obj(df)
# Preset plot usage
bar_obj = bar_chart(df,
            x = "Kinds", 
            y = "Popularity",
            title= "1.Using preset plot function `bar_chart()`"
            )
# Animate with defined arguments 
anim_obj = beta_vizzu_animate( bar_obj,
    x = "Genres",
    y =  ["Popularity", "Kinds"],
    title = "2.Animate with:arg specific `beta_vizzu_animate()`",
    label= "Popularity",
    color="Genres",
    legend="color",
    sort="byValue",
    reverse=True,
    align="center",
    split=False,
)
_dict = {"size": {"set": "Popularity"}, 
    "geometry": "circle",
    "coordSystem": "polar",
    "title": "3.Animate with: generic dict-based `vizzu_animate()`",
    }

# Animate with general dict based arguments 
anim_obj2 = vizzu_animate(anim_obj,_dict)
# Visualize
with st.container():
    st.button("Animate ♻️ ")
    vizzu_plot(anim_obj2)    
with st.expander("Data",expanded=False):
    df
# Updating Readme 
import glob
import os
with open(f'README.md', 'r') as f:
    readme_lines = f.readlines()
    readme_buffer = []
    resource_files = [os.path.basename(x) for x in glob.glob(f'Resources/*')]
for line in readme_lines:
    readme_buffer.append(line)
    for image in resource_files:
        if image in line:
            st.markdown(' '.join(readme_buffer[:-1]))
            st.image(f'Resources/{image}')
            readme_buffer.clear()   
st.markdown(' '.join(readme_buffer))
