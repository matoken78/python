# https://dash.plot.ly

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def _make_bar():
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    app.layout = html.Div(
        style={'backgroundColor': colors['background']},
        children=[
            html.H1(
                children='Hello Dash',
                style={'textAlign': 'center', 'color': colors['text']}),
            html.Div(
                children='Dash: A web application framework for Python.',
                style={'textAlign': 'center', 'color': colors['text']}),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Motreal'},
                    ],
                    'layout': {
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        },
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]
    )

def _generate_table(df, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # Body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(min(len(df), max_rows))]
    )

def _make_table():
    df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        'c78bf172206ce24f77d6363a2d754b59/raw/'
        'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
        'usa-agricultural-exports-2011.csv')
    app.layout = html.Div(
        children=[
            html.H4(children='US Agriculture Exports (2011)'),
            _generate_table(df)
    ])

def _make_scatter():
    df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        '5d1ea79569ed194d432e56108a04d188/raw/'
        'a9f9e8076b837d541398e999dcbac2b2826a81f8/'
        'gdp-life-exp-2007.csv')
    app.layout = html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure={
                'data': [
                    go.Scatter(
                        x=df[df['continent'] == i]['gdp per capita'],
                        y=df[df['continent'] == i]['life expectancy'],
                        text=df[df['continent'] == i]['country'],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name = i
                    ) for i in df.continent.unique()
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                    yaxis={'title': 'Life Expectancy'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])

def _make_markdown():
    markdown_text = '''
        ### Dash and Markdown

        Dash apps can be written in Markdown.
        Dash uses the [CommonMark](http://commonmark.org/)
        specification of Markdown.
        Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
        if this is your first introduction to Markdown!
        '''

    app.layout = html.Div([
        dcc.Markdown(children=markdown_text)
    ])

def _make_parts():
    app.layout = html.Div([
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            # ここに選択した値が入る（ここではデフォルト値を設定している）
            value='MTL'
        ),

        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            # 複数の選択を可能にする引数
            multi=True
        ),

        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        ),

        html.Label('Checkboxes'),
        dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            # リスト型で与えていることに注意
            value=['MTL', 'SF']
        ),

        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) 
                if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    # 表示を2列に分けるstyleを設定
    ], style={'columnCount': 1})

if __name__ == '__main__':
    # _make_bar()
    # _make_table()
    # _make_scatter()
    # _make_markdown()
    _make_parts()
    app.run_server(debug=True)