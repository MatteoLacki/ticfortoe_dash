import dash

settings = {
    "HOST": "0.0.0.0",
    "DEBUG": True,
    "THEME": "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css",
    "SIDEBAR_STYLE": dict(
        position="fixed", top=0, left=0, bottom=0, width="16rem", padding="2rem 1rem"
    ),
    "CONTENT_STYLE": {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    },
}


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[settings["THEME"]],
)
