import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

myheading='Pick your 2020 Democratic presidential candidate'
tabtitle='2020'
mytitle = 'Chart'
dem_candidates=('Warren', 'Biden', 'Sanders', 'Buttigieg')
poll_dates=['July', 'August', 'September', 'October']
poll_data=[[20,23,33,45],[22,29,27,26],[13,15,16,10],[12,10,9,7]]
color_ew='#fc8403'
color_jb='#0317fc'
color_bs='#9013fc'
color_pb='#05F935'

trace0 = go.Scatter(
    x = poll_dates,
    y = poll_data[0],
    mode = 'lines',
    marker = {'color': color_ew},
    name = dem_candidates[0]
)
trace1 = go.Scatter(
    x = poll_dates,
    y = poll_data[1],
    mode = 'lines',
    marker = {'color': color_jp},
    name = dem_candidates[1]
)
trace2 = go.Scatter(
    x = poll_dates,
    y = poll_data[2],
    mode = 'lines',
    marker = {'color': color_bs},
    name = dem_candidates[2]
)
trace3 = go.Scatter(
    x = poll_dates,
    y = poll_data[3],
    mode = 'lines',
    marker = {'color': color_pb},
    name = dem_candidates[3]
)

data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    )
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
