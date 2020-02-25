from typing import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

uvxy_df = pd.read_csv('UVXY.csv')
vix_df = pd.read_csv('vixcurrent.csv')

print(type(uvxy_df))

uvxy_fig = px.line(uvxy_df, x='Date', y='High', title='UVXY Price over time')
uvxy_fig.update_layout(yaxis_type="log")
vix_fig = px.line(vix_df, x='Date', y='VIX High', title='VIX number over time')

print(type(uvxy_fig))

uvxy_fig.show()
vix_fig.show()
