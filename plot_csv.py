import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pandas import *
from plotly.graph_objs._figure import *

with open('vixcurrent.csv', 'r') as file_out:
    with open('vixcurrent_fixed.csv', 'w') as file_in:
        next(file_out)   # get rid of first line
        for line in file_out:
            file_in.write(line)

uvxy_df: DataFrame = pd.read_csv('TVIX.csv')
vix_df: DataFrame = pd.read_csv('vixcurrent_fixed.csv')

uvxy_fig: Figure = go.Figure(go.Scatter(x=uvxy_df['Date'], y=uvxy_df['High'], name='high', mode='lines'))
uvxy_fig.add_trace(go.Scatter(x=uvxy_df['Date'], y=uvxy_df['Close'], name='close', mode='lines'))
uvxy_fig.update_layout(yaxis_type="log", title="UVXY price")

vix_fig: line = px.line(vix_df, x='Date', y='VIX High', title='VIX number over time')
vix_fig.update_layout(yaxis_type="log")

uvxy_fig.show()
vix_fig.show()
