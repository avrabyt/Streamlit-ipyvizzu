import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
from streamlit.components.v1 import html
import streamlit as st

st.set_page_config(page_title="Streamlit-ipyvizzu", layout="centered")
st.sidebar.title("Bubble Chart-Demo")
data_frame = pd.read_csv(
    "Data/chart_types_eu.csv", dtype={"Year": str, "Timeseries": str}
)
with st.expander("Data  ⤵️"):
    st.dataframe(data_frame)

# Initialize <class 'ipyvizzu.animation.Data'>
data = Data()
data.add_data_frame(data_frame)
# A class for representing a wrapper over Vizzu chart. <class 'ipyvizzu.chart.Chart'>
chart = Chart(display="manual")
# A method for animating the chart.
chart.animate(data)

chart.animate(
    Config(
        {
            "channels": {
                "color": {"set": ["Joy factors"]},
                "size": {"set": ["Value 2 (+)"]},
                "label": {"set": ["Country_code"]},
            },
            "title": "Bubble Chart",
            "geometry": "circle",
        }
    )
)


_t = ["Value 2 (+)", "Country_code"]
_t = [ "Value 2 (+)","Country_code"]
chart.animate(
    Config(
        {
            "channels": {"size": {"set": _t}},
            "title": "Stacked Bubble Chart",
        }
    ),
    Style({"plot": {"marker": {"label": {"fontSize": 10}}}}),
)

html(chart._repr_html_(), width=700, height=600)
st.sidebar.button("Animate ♻️")