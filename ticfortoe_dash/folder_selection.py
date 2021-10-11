import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from dash.dependencies import Input, Output, State
from dash import dash_table

from config import get_all_files, ask_for_paths_df
from ticfortoe_dash.app import app


NAME = "Folder Selection"
uid = "folder_selection"  # unique identifier for app elements


default_paths = get_all_files()
print(default_paths)

layout = html.Div(
    [
        html.H1("Find Paths"),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dbc.Row(dbc.Textarea(id=f"{uid}_search_area")), width=5),
                dbc.Col(
                    dbc.Button(
                        "Search!",
                        id=f"{uid}_search",
                        color="primary",
                        block=True,
                        style={"height": "100%"},
                    ),
                    width=1,
                ),
                dbc.Col(
                    [
                        html.Div(id=f"{uid}_search_stats"),
                        dash_table.DataTable(
                            id=f"{uid}_found_paths",
                            columns=[
                                {"name": col, "id": col}
                                for col in default_paths.columns
                            ],
                            data=default_paths.to_dict("records"),
                            page_size=25,
                            filter_action="native",
                        )
                    ],
                    width=5,
                ),
                dbc.Col(
                    dbc.Button(
                        "Energize!",
                        color="primary",
                        block=True,
                        style={"height": "100%"},
                    ),
                    width=1,
                ),
            ]
        ),
    ]
)


@app.callback(
    [
        Output(f"{uid}_found_paths", "data"),
        Output(f"{uid}_search_stats", "value")
    ],
    Input(f"{uid}_search", "n_clicks"),
    State(f"{uid}_search_area", "value"),
)
def search(number_of_clicks, patterns):
    if patterns:
        res = ask_for_paths_df(patterns.split(" "))
        stats = f"Found {len(res)} folders."
        return res.to_dict("records"), stats
