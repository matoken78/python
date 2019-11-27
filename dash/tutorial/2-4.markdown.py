# https://dash.plot.ly

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def _make_markdown():
    markdown_text = '''
        ### Dash and Markdown

        Dash apps can be written in Markdown.
        Dash uses the [CommonMark](http://commonmark.org/)
        specification of Markdown.
        Check out their
        [60 Second Markdown Tutorial](http://commonmark.org/help/)
        if this is your first introduction to Markdown!
        '''

    app.layout = html.Div([
        dcc.Markdown(children=markdown_text)
    ])


if __name__ == '__main__':
    _make_markdown()
    app.run_server(debug=True)
