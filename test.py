from st_vizzu import *
import pandas as pd

# Load Data
df = pd.read_csv("Data/eu_regions.csv",sep=';')
# Plots
h = bar_chart(DataFrame = df, y = "Population (2020)", x = "Country")
vizzu_plot(h)
vizzu_plot(stacked_bubble_chart(df,size="Population (2020)",color="Country",stackedBy="Subregion"))
