import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv("udemy_courses_extended.csv", usecols=range(1, 12))

sorted_df = df.groupby('is_paid').agg(
                courses_count=('is_paid', 'count'),
                max_subs=('num_subscribers', 'max'),
                mean_subs=('num_subscribers', 'mean'),
                min_subs=('num_subscribers', 'min'),
                begginer_courses_count=('level', lambda x: sum(x == 'Beginner Level')),
                intermediate_courses_count=('level', lambda x: sum(x == 'Intermediate Level')),
                expert_courses_count=('level', lambda x: sum(x == 'Expert Level')),
                all_levels_count=('level', lambda x: sum(x == 'All Levels'))
            )


fig = go.Figure(data=[
    go.Bar(name="Courses count",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 0]),
    go.Bar(name="Max subscribers",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 1]),
    go.Bar(name="Mean subscribers",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 2]),
    go.Bar(name="Min subscribers",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 3]),
    go.Bar(name="Beginner Courses Count",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 4]),
    go.Bar(name="Intermediate Courses Count",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 5]),
    go.Bar(name="Expert Courses Count",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 6]),
    go.Bar(name="All Levels Courses Count",
           x=sorted_df.iloc[:, 0].index.values, 
           y=sorted_df.iloc[:, 7])       
])

fig.update_layout(xaxis_title="Is Free")
fig.update_layout(barmode='group')
fig.update_layout(title="Информация по курсам Udemy")
fig.show()