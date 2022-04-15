import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

#data
df = pd.read_csv('data/aapl data.csv')



tabtitle = 'AAPL Stock Info'
sourceurl = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
githublink = 'https://github.com/moris96/AAPL-Stock-Data'




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

# run app
app.run_server(debug=True)