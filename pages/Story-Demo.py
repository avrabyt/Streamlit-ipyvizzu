from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import ssl
import streamlit as st 
ssl._create_default_https_context = ssl._create_unverified_context  

def create_chart():
    # initialize chart
    data = Data()
    df = pd.read_csv(
        "https://raw.githubusercontent.com/petervidos/vizzu-pres/main/Prog_lang_popularity2.csv", dtype={"Year": str},
    )
    data.add_data_frame(df)
    #@title Create the story
    story = Story(data=data)
    #story.set_size("100%", "450px")
    story.set_size(800, 450)
    label_handler_method = "if(event.data.text.split(' ')[0] < 5) event.preventDefault()"

    story.add_event("plot-marker-label-draw", label_handler_method)

    slide2_1 = Slide(
        Step(
            Data.filter("record.Year == 2022"), 
            Config({
                "x": ["Popularity","Value[%]"], 
                "y": ["Language","Year","Lang_year"],
                "color": "Popularity",
                "label": "Value[%]",
                "align": "stretch",
                "title": "Use of programming languages by data scientists in 2022",
                "lightness":"Year",
                "legend":"color"
            }),
            Style({"logo": {"width": "5em"},"plot": {"xAxis": {"title":{"color": "#00000000"}},"paddingLeft": "2.5em","marker": {"colorPalette": "#3DAE2BFF #00833EFF #00A19BFF #0075A9FF #003764FF",
            "minLightness":0, "maxLightness":0.4}
            }})
        )
    )
    story.add_slide(slide2_1)

    slide2_2 = Slide(
        Step(Config({
                "split": True,"align": "min", "title": "Python is always or frequently used by 58%"
        }),
            Style({"plot": {"xAxis": {"label":{"color": "#00000000"}}
            }})
        )
    )
    story.add_slide(slide2_2)

    slide2_3 = Slide()

    slide2_3.add_step(
        Step(Config({
            "split": False, "align": "stretch"
        }),
            Style({"plot": {"xAxis": {"label":{"color": "#999999FF"}}
            }}))
    )

    slide2_3.add_step(
        Step(
            Data.filter("(record.Popularity == 'Always' || record.Popularity == 'Frequently') && record.Year == 2022"),
            Config({"x":{"range":{"max":100}},"align":"min"})
        )
    )

    slide2_3.add_step(
        Step(
            Config({"sort":"byValue","title":"Python & SQL are the most popular by a huge margin"})
        )
    )
    story.add_slide(slide2_3)

    slide2_4 = Slide()

    slide2_4.add_step(
        Step(
            Config({"sort":"none","title":"Let's focus on the six languages with data since 2020"})
        )
    )

    slide2_4.add_step(
        Step(
            Data.filter("(record.Popularity == 'Always' || record.Popularity == 'Frequently') && (record.Language == 'R' || record.Language == 'Python' || record.Language == 'JavaScript' || record.Language == 'Java' || record.Language == 'C#' || record.Language == 'C/C++')  && record.Year == 2022"),
        )
    )

    slide2_4.add_step(
        Step(
            Config({"y":["Lang_year","Year"],"x": ["Popularity","Language","Value[%]"], })
        )
    )
    story.add_slide(slide2_4)

    slide2_5 = Slide()

    slide2_5.add_step(
        Step(
            Data.filter("(record.Popularity == 'Always' || record.Popularity == 'Frequently') && (record.Language == 'R' || record.Language == 'Python' || record.Language == 'JavaScript' || record.Language == 'Java' || record.Language == 'C#' || record.Language == 'C/C++')   && record.Year != 2020"),
        )
    )

    slide2_5.add_step(
        Step(
            Data.filter("(record.Popularity == 'Always' || record.Popularity == 'Frequently') && (record.Language == 'R' || record.Language == 'Python' || record.Language == 'JavaScript' || record.Language == 'Java' || record.Language == 'C#' || record.Language == 'C/C++')"),
            Config({"title":"C/C++, C#, Java and Javascript are gaining popularity"})
        )
    )

    story.add_slide(slide2_5)

    # Switch on the tooltip that appears when the user hovers the mouse over a chart element.
    story.set_feature("tooltip", True)

    # story.play()

    return story,story._repr_html_(),df


obj,CHART,df = create_chart()
with st.container():
    html(CHART, width=800, height=600)

from streamlit_extras.mention import mention
with st.sidebar:
    mention(
        label="Resources",
        icon="twitter",  # Some icons are available... like Streamlit!
        url="https://twitter.com/VizzuHQ/status/1575473747599007744",
    )