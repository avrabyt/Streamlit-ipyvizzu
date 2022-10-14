# Stvizzu (# Streamlit-ipyvizzu)
[ipyvizzu](https://github.com/vizzuhq/ipyvizzu) wrapper for intuitive usage of ipyvizzu functions and Streamlit embed support.

<table>
    <tr>
        <td>Latest Release</td>
        <td>
            <a href="https://pypi.org/project/st-vizzu/"/>
            <img src="https://static.pepy.tech/badge/st-vizzu"/>
        </td>
    </tr>
    <tr>
        <td>PyPI Downloads</td>
        <td>
            <a href="https://pepy.tech/project/st-vizzu"/>
            <img src="https://static.pepy.tech/badge/st-vizzu/month"/>
        </td>
    </tr>
</table>

## Installation 
```console
pip install st-vizzu
```
## Example

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://avrabyt-streamlit-ipyvizzu-app-f69fjd.streamlitapp.com)

### Quickstart
```python
from st_vizzu import *
import pandas as pd
import streamlit as st

st.code("st_vizzu version: " + st_vizzu.__version__)
# Load Data
df = pd.read_csv("Data/music_data.csv", index_col=0)
# Create ipyvizzu Object with the DataFrame
obj = create_vizzu_obj(df)

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

# Animate with general dict based arguments 
_dict = {"size": {"set": "Popularity"}, 
    "geometry": "circle",
    "coordSystem": "polar",
    "title": "Animate with vizzu_animate () function",
    }
anim_obj2 = vizzu_animate(anim_obj,_dict)

# Visualize within Streamlit
with st.container(): # Maintaining the aspect ratio
    st.button("Animate")
    vizzu_plot(anim_obj2)

```


## Animated charts ✨
![Animation](https://github.com/avrabyt/Streamlit-ipyvizzu/blob/main/Resources/animation.gif)

## Story-presentation ⌛️
![Animation](https://github.com/avrabyt/Streamlit-ipyvizzu/blob/main/Resources/story.gif)
