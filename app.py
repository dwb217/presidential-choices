import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

myheading1='Pick your 2020 Democratic presidential candidate'
tabtitle='2020'
dem_candidates=['Warren', 'Biden', 'Sanders', 'Buttigieg']
poll_data=[(20,23,33,45),(22,29,27,26),(13,15,16,10),(12,10,9,7)]
color_ew='#fc8403'
color_jb='#0317fc'
color_bs='#9013fc'
color_pb='#05F935'

trace0 = go.Scatter(
    x = dem_candidates,
    y = poll_data,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3

trace3 = go.Scatter(
    x = x_values,
    y = y4_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name4
)
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
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()

