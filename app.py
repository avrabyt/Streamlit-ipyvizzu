from st_vizzu import *
import pandas as pd
import streamlit as st
from streamlit_extras.badges import badge

from st_pages import Page,Section, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("app.py", "st-vizzu (Streamlit-ipyvizzu)", "🎈️"),
        Page("pages/Basic-Demo.py", "Example 1 (Basic)", "📊"),
        Page("pages/Story-Demo.py","Example 2 (Story)","🎥"),
        Page("pages/BubbleChart.py","Example 3 (Bubble-Chart)","💭" ),
        Page("pages/Netflix-EDA.py","Example 4 (EDA)","👨🏾‍💻"),
        Page("pages/Workarounds.py","Example 5 (Workarounds)","🍀")
    ]
)

badge(type="github", name="avrabyt/Streamlit-ipyvizzu")
# st.markdown(''' 
#             ### Create animated charts easily! 
#             A [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) wrapper for intuitive usage of ipyvizzu functions and Streamlit embed support. 
            
#             ''')
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
    vizzu_plot(anim_obj2) 
    st.button("Animate ♻️ ")
       
# with st.expander("Data",expanded=False):
#     df

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
