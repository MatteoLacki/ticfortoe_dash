import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from dash.dependencies import Input, Output, State
from dash import dash_table

from config import get_all_files


NAME = "Upload Center"
uid = "uploads" # unique identifier for app elements


default_paths = get_all_files()
print(default_paths)

layout = html.Div([
    html.H1("Uploads"),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Row(html.P("Paste below the names of the raw folders separated by spaces:")),
            dbc.Row(dbc.Textarea())                
        ], width=6),
        dbc.Col([
            dash_table.DataTable(
                id=f"{uid}_found_paths",
                columns=[
                    {"name": col, "id": col}
                    for col in default_paths.columns],
                data=default_paths.to_dict("records"),
                page_size=10,
                filter_action="native",
            )
        ], width=6),
    ]),
    dbc.Button("Energize!", color="primary", block=True)
])





