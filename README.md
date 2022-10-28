# Streamlit-ipyvizzu (st-vizzu)

**Create animated charts easily! A [ipyvizzu](https://github.com/vizzuhq/ipyvizzu)  wrapper for intuitive usage of ipyvizzu functions and Streamlit embed support.**

[![PyPI version](https://badge.fury.io/py/st-vizzu.svg)](https://badge.fury.io/py/st-vizzu)
[![Downloads](https://static.pepy.tech/personalized-badge/st-vizzu?period=month&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/st-vizzu)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://hellostvizzu.streamlitapp.com/)



## Installation 
```console
pip install st-vizzu
```

## Workflow simplification 

1. **Create** ipyvizzu object using,
`create_vizzu_obj()`
or define preset ipyvizzu charts for example,bar charts using, `bar_chart()`

2. **Animate** the charts using, _generalized_ function, `vizzu_animate()` or _argument specific_ function, `beta_vizzu_animate()`

3. **Embed** the charts within Streamlit front-end using, `vizzu_plot()`

### Quickstart
```python
from st_vizzu import *
import pandas as pd
import streamlit as st

# Load Data
df = pd.read_csv("Data/music_data.csv", index_col=0)
# Create ipyvizzu Object with the DataFrame
obj = create_vizzu_obj(df)

# Preset plot usage. Preset plots works directly with DataFrames.
bar_obj = bar_chart(df,
            x = "Kinds", 
            y = "Popularity",
            title= "1.Using preset plot function `bar_chart()`"
            )

# Animate with defined arguments 
anim_obj = beta_vizzu_animate( bar_obj,
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

## Example

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hellostvizzu.streamlitapp.com/)

### Animated charts ✨
![Animation1](https://github.com/avrabyt/Streamlit-ipyvizzu/blob/main/Resources/animation.gif)

### Story-presentation ⌛️
![Story](https://github.com/avrabyt/Streamlit-ipyvizzu/blob/main/Resources/story.gif)

## Resources 
- [Streamlit Multi-Page Configuration](https://github.com/blackary/mpa-config) - The demo app uses custom config file for Multipage Layout. Thanks to @blackary
- [streamlit-extras](https://github.com/arnaudmiribel/streamlit-extras) - A Python library with useful Streamlit extras . Thanks @arnaudmiribel
- [ipyvizzu](https://github.com/vizzuhq/ipyvizzu)
- [Streamlit](https://discuss.streamlit.io/)

