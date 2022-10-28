import ssl
import pandas as pd
from ipyvizzu import Data, Config, Style
from streamlit.components.v1 import html
import streamlit as st
from ipyvizzustory import Story, Slide, Step
from st_vizzu import *
# works with streamlit version streamlit==1.13.0
from page_config import standard_page_widgets
# Add this on top of any page to make mpa-config work!
standard_page_widgets()

ssl._create_default_https_context = ssl._create_unverified_context
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def non_static_chart(df):
    bar_obj = bar_chart(df,x="Language", y= "Value[%]", title= "A simple bar plot that will re-animate on clicks.")
    static_html = bar_obj._repr_html_()
    return static_html

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def static_chart(df):
    bar_obj = bar_chart(df,x="Language", y= "Value[%]", title= "A simple static bar plot at the Streamlit front-end.")
    static_html = bar_obj._repr_html_()
    return static_html

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def create_chart(data):
    obj = create_vizzu_obj(data)
    title_Str = "Use of programming languages by data scientists."
    config_dict = {
                "x": ["Popularity","Value[%]"], 
                "y": ["Language","Year","Lang_year"],
                "color": "Popularity",
                "label": "Value[%]",
                "align": "stretch",
                "title": title_Str,
                "lightness":"Year",
                "legend":"color"
            }
    style_dict = {"logo": {"width": "5em"},
                "plot": {"xAxis": {"title":{"color": "#00000000"}},
                "marker": {"colorPalette": "#3DAE2BFF #00833EFF #00A19BFF #0075A9FF #003764FF",
                "minLightness":0, "maxLightness":0.4}
            }}
   
    # Animate 1
    anim_obj1  = vizzu_animate(obj=obj,config_dict=config_dict,style_dict=style_dict)
    # Animate 2
    anim_obj2 = beta_vizzu_animate(obj = anim_obj1, 
                x =  ["Popularity","Value[%]"], 
                y = ["Language","Year","Lang_year"],
                color = "Popularity",
                label = ["Popularity"],
                tooltip= True,
                split=True)  
    vizzu_html = anim_obj2._repr_html_()
    return vizzu_html

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def create_story(df):   
    # initialize chart
    data = Data()
    data.add_data_frame(df)    
    #@title Create the story
    story = Story(data=data)
    story.set_size(800, 450)
    label_handler_method = "if(event.data.text.split(' ')[0] < 5) event.preventDefault()"
    story.add_event("plot-marker-label-draw", label_handler_method)
    title_Str = "Use of programming languages by data scientists."
    slide2_1 = Slide(
        Step(           
            Config({
                "x": ["Popularity","Value[%]"], 
                "y": ["Language","Year","Lang_year"],
                "color": "Popularity",
                "label": "Value[%]",
                "align": "stretch",
                "title": title_Str,
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
    story.set_feature("tooltip", True)
    html = story._repr_html_()
    return html, story

# -- App ---- 
st.title("A recent story of Programming Languages! 🌟")
st.warning("A simple demonstration to avoid _'Streamlit-Reloading problem'_ .")


st.sidebar.markdown('''
    # Sections
    - [Reloading issue](#non-static-chart)
    - [Static chart here](#static-chart)
    - [Animated charts here](#animated-charts)
    - [Ipyvizzu-story here](#visualize-data-story)
    - [Selected data](#selected-data)
    
    ''', unsafe_allow_html= True)

#Load Data
story_data = pd.read_csv("https://raw.githubusercontent.com/petervidos/vizzu-pres/main/Prog_lang_popularity2.csv", dtype={"Year": str},)

# The problem !!
st.subheader('Non-static-chart')
st.info("The chart is interactive with `Streamlit widget` changes. It reanimates on every widget (buttons,checkbox etc) click ...",icon="ℹ️" )
with st.expander("Expand to view the non-Static Chart !", expanded=True):
    with st.container():
        ns_html = non_static_chart(story_data)
        html(ns_html,width=900,height=450)
        if st.button("I can Animate ♻️"):
            st.info("As I said, chart will REANIMATE. It RELOADS on every interaction with the app ...", icon="ℹ️")


# Static Demo - Because it depends on the loaded data
st.subheader('Static-chart')
st.info("The chart is NOT interactive with `Streamlit widget` changes. It stayts as it is forever ...",icon="ℹ️" )
with st.expander("Expand to view the Static Chart !", expanded=True):
    with st.container():
        s_html = static_chart(story_data)
        html(s_html,width=900,height=450)
        if st.button("Try me to animate ♻️"):
            st.info("Gotcha! As I said, the chart will NOT reanimate. Check data-dependent reanimation below 'Animated charts' .", icon="✖")

# Working with Widgets
sel_year = st.sidebar.selectbox("Tell me the year you want to visualize", options = story_data["Year"].unique())
lang_opt = story_data["Language"].unique()
sel_language= st.sidebar.multiselect("Tell me the language(s) you want to visualize", options = lang_opt, 
                            default=["Python", "JavaScript", "HTML/CSS", "C/C++"] )
# Filter DataFrame
sel_data_langbased = story_data[story_data["Language"].isin(sel_language)]
sel_data = sel_data_langbased[story_data["Year"] == sel_year]
# Download DataFrame
csv = convert_df(sel_data)
st.sidebar.download_button(
    label="Download selected data as CSV",
    data = csv,
    file_name='selected_data.csv',
    mime='text/csv',
)

st.sidebar.info("Data (rows) : " + str(len(sel_data)))
v_html = create_chart(sel_data)
st.subheader('Animated-charts')
st.info("The chart is interactive with `Streamlit widget` change.  Reloads ONLY when there is a change in selected data. ",icon="✔️" )
html(v_html,width=950,height=450)
if st.button("Try to reanimate animated charts! ♻️"):
    st.info("Gotcha! As I said, the chart will NOT reanimate. Tweak `year` and `language` : it may reanimate. ", icon="✖")
st.subheader('Visualize-data-story')
st.info("The story is NOT interactive with `Streamlit widget` changes. Treat it as a story of the whole data. Press respective `button(s)` to generate and download.",icon="ℹ️" )
if st.sidebar.button("Generate Story"):
    story_html, slides = create_story(story_data)    
    with st.container():
        html(story_html, width=800, height=500)        
        st.sidebar.download_button(label = 'Download Story',
                        data = slides.to_html(),
                        file_name = "my_story.html",
                        )
        st.success("Don't forget to download the story!",icon="✅")
else:
    st.warning("Press  `Generate Story` button to view the story.")
# Display dataframe
st.subheader('Selected-data')
if st.sidebar.checkbox("Show me the data"):  
    with st.expander(label="Expand to view the selected data:", expanded=True):
        st.dataframe(sel_data)        
else:
    st.warning("Select the checkbox  `Show me the data` button view the story.")