import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# from ticfortoe_dash import folder_selection
from ticfortoe_dash import folder_selection_2
from ticfortoe_dash.app import app, settings


href2app = {
    "/": folder_selection_2,
    # "/folder_selection": folder_selection,
    "/folder_selection_2": folder_selection_2,
}


sidebar = html.Div(
    [
        html.H2("TIC for TOE"),
        html.H3("TIC calculator FOR The OthErs"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(_app.NAME, href=href, active="exact")
                for href, _app in href2app.items()
            ],
            vertical=True,
            pills=True,
        ),
        html.Div(id="store_contents"),
        html.Div(id="session_id"),
        dcc.Store(id="cookies", storage_type="session"),
    ],
    style=settings["SIDEBAR_STYLE"],
)

content = html.Div(id="page-content", style=settings["CONTENT_STYLE"])

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_content(pathname):
    try:
        return href2app[pathname].layout
    except AttributeError:
        return href2app[pathname].get_layout(cookies)
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


if __name__ == "__main__":
    app.run_server(host=settings["HOST"], debug=settings["DEBUG"])
