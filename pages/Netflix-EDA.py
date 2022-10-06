# https://www.kaggle.com/code/subinium/storytelling-with-data-netflix-ver/notebook
# https://ipyvizzu.vizzuhq.com/examples/examples.html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
from streamlit.components.v1 import html
import streamlit as st
import numpy as np
from collections import Counter


st.set_page_config(page_title="Streamlit-ipyvizzu", layout="wide")
st.sidebar.title("Netflix-EDA")
data = pd.read_csv('Data/netflix_titles.csv')
with st.expander("Expand to check the data  ⤵️"):
    st.dataframe(data)
data = data.fillna('NULL')
data['year_added'] = data['date_added'].apply(lambda x :  x.split(',')[-1])
data['year_added'] = data['year_added'].apply(lambda x : x if x != 'NULL' else '2020')
data['year_added'] = data['year_added'].apply(int)
movie = data[data['type'] == 'Movie']
tv_show = data[data['type'] == 'TV Show']
st.sidebar.button("Animate ♻️")
country_data = data['country']
country_counting = pd.Series(dict(Counter(','.join(country_data).replace(' ,',',').replace(', ',',').split(',')))).sort_values(ascending=False)
country_counting.drop(['NULL'], axis=0, inplace=True)
sl_value = st.sidebar.slider(label="No of countries to include?",
                            min_value=1,max_value=25,
                            value = 5, step=1)
top20_country = country_counting[:sl_value]
di = top20_country.to_dict()
col1,col2,col3 = st.columns([4,1,4])
with col1.container():
    st.subheader( " Top {} countries producing the most contents ".format(sl_value))
    ccdf = pd.DataFrame.from_dict(data=di,orient='index')
    ccdf["countries"] = ccdf.index
    ccdf["values"] = ccdf[0]
    ccdf = ccdf.drop(0,axis=1)
    # ccdf = ccdf.iloc[:sl_value]
    # st.write(type(di))

    dataC = Data()
    dataC.add_data_frame(ccdf)
    chart = Chart(width="400px", height="400px",display="manual")
    chart.animate(dataC)


    chart.animate(
        Config(
            {
                "channels": {
                    "color": {"set": ["countries"]},
                    "size": {"set": ["values"]},
                    "label": {"set": ["countries"]},
                },
                "title": "Treemap",
            }
        ),
        Style({"plot": {"marker": {"label": {"fontSize": 14}}}}),
    )

    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"set": ["values"]},
                    "y": {"set": ["countries"], "range": {"min": "-30%"}},
                    "size": {"set": None},
                    "label": {"set": ["countries"]},
                },
                "title": "Radial Chart",
                "coordSystem": "polar",
            }
        )
    )
    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"detach": ["countries"]},
                    "label": {"set": ["values"]},
                }
            }
        ),
        Style(
            {
                "plot": {
                    "marker": {"label": {"fontSize": None}},
                    "xAxis": {
                        "title": {"color": "#ffffff00"},
                        "label": {"color": "#ffffff00"},
                        "interlacing": {"color": "#ffffff00"},
                    },
                    "yAxis": {"color": "#ffffff00", "label": {"paddingRight": 20}},
                }
            }
        ),
    )
    html(chart._repr_html_(),width=500, height=500)
    
with col3.container():
    st.subheader(" Time consumption compared across top {} countries ".format(sl_value))
    
    data['country'] = data['country'].dropna().apply(lambda x :  x.replace(' ,',',').replace(', ',',').split(','))
    lst_col = 'country'
    data2 = pd.DataFrame({
        col : np.repeat(data[col].values, data[lst_col].str.len())
    for col in data.columns.drop(lst_col)
    }
    ).assign(**{lst_col:np.concatenate(data[lst_col].values)})[data.columns.tolist()]
    year_country = data2.groupby('year_added')['country'].value_counts().reset_index(name='counts')
    # year_country
    year_country['top20'] = year_country['country'].apply(lambda x : x in top20_country.index)
    year_country = year_country[(year_country['year_added'] >= 1990) & year_country['top20'] & (year_country['year_added'] < 2020)] 
    year_country["year_added"] = year_country["year_added"].astype(str)
    
    datav = Data()
    datav.add_data_frame(year_country)
    chart = Chart(width="500px", height="500px",display="manual")
    chart.animate(datav)

    chart.animate(
        Config.stream(
            {
                "x": "year_added",
                "y": "counts",
                "stackedBy": "country",
                "title": "Stream Graph",
            }
        ),
        Style(
            {
                "plot": {
                    "paddingLeft": "1.2em",
                    "yAxis": {
                        "label": {"paddingRight": "0.8em"},
                        "interlacing": {"color": "#ffffff00"},
                    },
                    "xAxis": {"label": {"paddingTop": "0.8em", "angle": "-45deg"}},
                }
            }
        ),
    )
    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"set": ["year_added"]},
                    "y": {"set": ["counts", "country"]},
                    "color": {"set": ["country"]},
                },
                "title": "Stacked Area Chart",
                "geometry": "area",
            }
        ),
    )
    chart.animate(Config({"title": "100% Stacked Area Chart", "align": "stretch"}))
    chart.animate(
    Config(
        {
            "channels": {"y": {"range": {"max": "100%"}}},
            "title": "Trellis (Splitted) Area Chart",
            "align": "min",
            "split": True,
        }
    )
    )
    html(chart._repr_html_(),width=700, height=600)


with st.expander(label=" ", expanded=True):
    col1,col2,col3 = st.columns(3)
    year_country2 = data2.groupby('year_added')['country'].value_counts().reset_index(name='counts')
    year_country2["year_added"] = year_country2["year_added"].astype(str)
    # col1.subheader("Year-wise analysis:")
    yr = col1.selectbox("Select the year", options=year_country2["year_added"].unique(), index=7)
    year_country2 = year_country2[year_country2['year_added'].str.contains(yr)]
    # year_country2 = year_country2.iloc[:sl_value]
    col1.dataframe(year_country2)
    if yr:  
        data = Data()
        data.add_data_frame(year_country2)

        chart = Chart(width="500px", height="500px",display="manual")
        chart.animate(data)

        chart.animate(
        Config(
        {
            "channels": {
                "x": {"set": ["counts", "country"]},
                "color": {"set": ["country"]},
                "label": {"set": ["counts"]},
            },
            "title": "Year-wise Chart",
            "coordSystem": "polar",
        }
        )
        )
        chart.animate(
        Config({"channels": {"y": {"range": {"min": "-200%"}}}, "title": "Year-wise Donut"})
        )
    with col2:
        html(chart._repr_html_(),width=900, height=600)

st.sidebar.markdown("[Resources (Kaggle)](https://www.kaggle.com/code/subinium/storytelling-with-data-netflix-ver/notebook)")