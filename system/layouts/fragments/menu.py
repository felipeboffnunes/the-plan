
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(html.P("Musaeum"), id="musaeum-header"),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        html.Hr(id="line-logo"),
        html.P("not a university"),
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse([
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/home", active="exact"),
                    dbc.NavLink("About", href="/about", active="exact"),
                    dbc.NavLink("Wiki", href="https://wiki.musaeum.university")
                ],
                vertical=True,
                pills=True,
            ),
            html.Div([
                html.Hr(id="line-logo"),
                dbc.Col(html.P("Pyrrhic Buddha", id="pyrrhic-header")),
                dbc.Nav(
                    [
                        dbc.NavLink("Library", href="/library", active="exact"),
                        dbc.NavLink("Logbook", href="/logbook", active="exact"),
                        dbc.NavLink("Writing", href="/writing", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                )
            ], id="pyrrhic-sidebar")
            ],
            id="collapse",
        ),
    ],
    id="sidebar",
)