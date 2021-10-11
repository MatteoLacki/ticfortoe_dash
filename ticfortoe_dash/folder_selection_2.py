import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd

from dash.dependencies import Input, Output, State
from dash import dash_table

from config import search_paths_on_instrument, instrument2pattern
from ticfortoe_dash.app import app


NAME = "Folder Selection 2"
uid = "folder_selection_2"  # unique identifier for app elements


default_table = pd.DataFrame([{"path":"sda"}])
help_modal_text = """
# Test Info

* Maybe it works
* MAybe not.

"""


layout = html.Div(
    [
        dbc.Row(
            [   
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id=f"{uid}_instrument_selection",
                            options=[ 
                                {"label": ins, "value": ins}
                                for ins in instrument2pattern
                            ],
                            searchable=False,
                            placeholder='Select the Instrument'
                        ),
                    ],
                    width=11
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            "Info",
                            id=f"{uid}_info_button",
                            color="primary",
                            block=True,
                            style={"height": "100%"},
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalBody(dcc.Markdown(help_modal_text)),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "So easy!",
                                        id=f"{uid}_close_modal_button",
                                        className="ml-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id=f"{uid}_info_modal",
                            is_open=False,
                            size="lg",
                        )
                    ],
                    width=1
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            id=f"{uid}_found_paths",
                            data=default_table.to_dict("records"),
                            columns=[
                                {"name":"file", "id":"file"},
                                {"name":"path", "id":"path"},
                                {"name":"date", "id":"date"}
                            ],
                            filter_action="native",
                            # row_selectable="multi",
                            sort_action="native",
                            page_size=10,
                            row_deletable=True,  
                        ),
                    ],
                    width=11,
                ),
                dbc.Col(
                    dbc.Button(
                        "To Basket!",
                        id="{uid}_add_to_selection_button",
                        color="primary",
                        block=True,
                        style={"height": "100%"},
                    ),
                    width=1,
                ),
            ]
        ),
        html.Br(),
        html.H3("Selected Folders:"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            id=f"{uid}_selected_paths_table",
                            data=default_table.to_dict("records"),
                            columns=[
                                {"name":"file", "id":"file"},
                                {"name":"path", "id":"path"},
                                {"name":"date", "id":"date"}
                            ],
                            filter_action="native",
                            # row_selectable="multi",
                            sort_action="native",
                            page_size=10,
                            row_deletable=True,  
                        )       
                    ], 
                    width=11
                ),
                dbc.Col(
                    dbc.Button(
                        "Fuck it!",
                        id="{uid}_calculate_button",
                        color="primary",
                        block=True,
                        style={"height": "100%"},
                    ),
                    width=1,
                ),
            ]
        )
    ]
)


@app.callback(
    Output(f"{uid}_info_modal", "is_open"),
    [
        Input(f"{uid}_info_button", "n_clicks"),
        Input(f"{uid}_close_modal_button", "n_clicks"),
    ],
    [State(f"{uid}_info_modal", "is_open")],
)
def info_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output(f"{uid}_found_paths", "data"),
    Input(f"{uid}_instrument_selection", "value")
)
def fetch_paths(instrument):
    if instrument:
        res = search_paths_on_instrument(instrument)
        return list(res.to_dict("records"))


@app.callback(
    Output(f"cookies", "data"),
    Input(f"{uid}_add_to_selection_button", "n_clicks"),
    State(f"{uid}_found_paths", "derived_virtual_selected_rows")
)
def fetch_paths(n_clicks, rows):
    if n_clicks:
        print("tu")
        print(n_clicks)
        print(rows)
        return {"selected_rows": rows}

