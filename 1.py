import plotly.express as px
import numpy as np
import pandas as pd

df = pd.read_csv("trees.csv", usecols=range(1, 4))
fig = px.imshow(df, text_auto=True, aspect="auto")
fig.show()
