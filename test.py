from st_vizzu import *
import pandas as pd
import streamlit as st
# Load Data
df = pd.read_csv("Data/music_data.csv", index_col=0)
df
# Plot Bar
bar_obj = bar_chart(df,
            x = "Genres", 
            y = "Popularity"
            )

# Animate
anim_obj = beta_vizzu_animate( bar_obj,
    x = {"set": "Genres"},
    y = {"set": "Popularity"}
)
anim_obj2 = beta_vizzu_animate(
    anim_obj,
    tooltip = True,
)
# Visualize
vizzu_plot(anim_obj._repr_html_())


