# https://dash.plot.ly

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def _make_callback_input_output():
    app.layout = html.Div([
        dcc.Input(id='my-id', value='initial value', type='text'),
        html.Div(id='my-div')
    ])

    @app.callback(
        Output(component_id='my-div', component_property='children'),
        [Input(component_id='my-id', component_property='value')]
    )
    def _update_output_div(input_value):
        return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    _make_callback_input_output()
    app.run_server(debug=True)
