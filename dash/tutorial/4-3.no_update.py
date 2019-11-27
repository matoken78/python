# https://dash.plot.ly

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def _make_dash_no_update():
    app.layout = html.Div([
        html.P('Enter a composite number to see its prime factors'),
        dcc.Input(id='num', type='number', debounce=True, min=1, step=1),
        html.P(id='err', style={'color': 'red'}),
        html.P(id='out')
    ])

    @app.callback(
        [Output('out', 'children'), Output('err', 'children')],
        [Input('num', 'value')]
    )
    def show_factors(num):
        if num is None:
            # PreventUpdate prevents ALL outputs updating
            raise PreventUpdate

        factors = prime_factors(num)
        if len(factors) == 1:
            # dash.no_update prevents any single output updating
            # (note: it's OK to use for a single-output callback too)
            return dash.no_update, '{} is prime!'.format(num)

        return '{} is {}'.format(num, ' * '.join(str(n) for n in factors)), ''

    def prime_factors(num):
        n, i, out = num, 2, []
        while i * i <= n:
            if n % i == 0:
                n = int(n / i)
                out.append(i)
            else:
                i += 1 if i == 2 else 2
        out.append(n)
        return out


if __name__ == '__main__':
    _make_dash_no_update()
    app.run_server(debug=True)
