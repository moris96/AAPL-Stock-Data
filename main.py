import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

#data
df = pd.read_csv('data/aapl data.csv')



tabtitle = 'AAPL vs MSFT'
sourceurl = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
githublink = 'https://github.com/moris96/AAPL-Stock-Data'


#plotly figure
fig = px.scatter(df, x="Date", y="Close", color="Stock")
fig.update_layout(
xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     step="day",
                     stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
fig.update_layout(
    height=800
)




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle


app.layout = html.Div([
    html.H1("AAPL vs MSFT Data for 2022 (as of April 14)"),
    dcc.Graph(figure=fig),
    html.A("Github", href=githublink),
    html.A("Data Source", href=sourceurl),
])








# run app
app.run_server(debug=True)