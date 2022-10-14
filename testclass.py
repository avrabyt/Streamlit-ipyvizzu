from st_vizzu import *
import pandas as pd

df = pd.read_csv("Data/music_data.csv", index_col=0)
obj = create_vizzu_obj(df)

v = stvizzu(x="Genres",y = "Popularity",title="")
vizzu_animate(obj,v.__dict__)
v.vizzu_show(obj=obj)


