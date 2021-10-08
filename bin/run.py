import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from ticfortoe_dash import uploads

settings = {
    "HOST": "0.0.0.0",
    "DEBUG": True,
    "THEME": "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css",
    "SIDEBAR_STYLE": dict(
        position = "fixed",
        top = 0,
        left = 0,
        bottom = 0,
        width = "16rem",
        padding = "2rem 1rem"
    ),
    "CONTENT_STYLE": {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem"
    }
}


href2app = {
    "/":            uploads,
    "/uploads":     uploads,
    "/visualize":   uploads
}

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[settings["THEME"]],
)


sidebar = html.Div(
    [
        html.H2("TIC for TOE"),
        html.H3("TIC calculator FOR The OthErs"),
        html.Hr(),
        dbc.Nav([
                dbc.NavLink(
                    _app.NAME,
                    href=href,
                    active="exact"
                )
                for href, _app in href2app.items()
            ],
            vertical=True,
            pills=True,
        ),
        html.Div(id='store_contents'),
        html.Div(id='session_id')
    ],
    style = settings["SIDEBAR_STYLE"],
)

content = html.Div(
    id="page-content",
    style=settings["CONTENT_STYLE"]
)

app.layout = html.Div([
    dcc.Location(id="url"), 
    sidebar,
    content
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_content(pathname):
    try:
        if pathname == "/uploads":
            return uploads.get_layout()
        elif pathname == "/QC":
            return QC.get_layout()
        else:
            return href2app[pathname].layout
    except KeyError:
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )
    except Exception as e:
        print(e)
        return repr(e)
 


if __name__ == '__main__':
    app.run_server(
        host=settings["HOST"],
        debug=settings["DEBUG"]
    )
