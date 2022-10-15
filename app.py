from st_vizzu import *
import pandas as pd
import streamlit as st

# st.code("st_vizzu version: " + st_vizzu.__version__)
# Load Data
df = pd.read_csv("Data/music_data.csv", index_col=0)
with st.expander("Data",expanded=False):
    df

# Create ipyvizzu Object
obj = create_vizzu_obj(df)
# Preset Plots
# bar_obj = bar_chart(df,
#             x = "Genres", 
#             y = "Popularity"
#             )
# Animate with defined arguments 
anim_obj = beta_vizzu_animate( obj,
    x = "Genres",
    y =  ["Popularity", "Kinds"],
    title = "Animate with beta_vizzu_animate () function",
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
    "title": "Animate with vizzu_animate () function",
    }

# Animate with general dict based arguments 
anim_obj2 = vizzu_animate(anim_obj,_dict)
# Visualize
with st.container():
    st.button("Animate")
    vizzu_plot(anim_obj2)

    
# with open(f'README.md', 'r') as f:           
#     st.markdown(f.read(),unsafe_allow_html=True)

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
