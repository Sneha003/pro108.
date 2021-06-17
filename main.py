import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/bell-curve--normal-distribution/master/data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"],show_hist=False)
fig.show()