import dash
import dash_bootstrap_components as dbc
from pathlib import Path
from json_schema_to_dash_forms import SchemaFormContainer
from dash.dependencies import Input, Output, State
import numpy as np
import json


# Font Awesome and bootstrap CSS required
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
external_stylesheets = [dbc.themes.BOOTSTRAP, FONT_AWESOME]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Required if using file browsing component
app.server.config['DATA_PATH'] = '.'

# The schema used to create the forms
path_schema = Path.cwd() / "schema.json"
with open(path_schema, 'r') as inp:
    my_schema = json.load(inp)

# Initialize
my_form = SchemaFormContainer(
    id='myform',
    schema=my_schema,
    parent_app=app
)

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            my_form,
            width={'size': 12}
        ),
    ),
    dbc.Row(
        dbc.Col(
            dbc.Button('Show data', id='show_data'),
            width={'size': 12}
        ),
        style={"margin-top": "10px", "margin-bottom": "10px"}
    ),
    dbc.Row([
        dbc.Col(
            dbc.Alert(
                children=[],
                id="alerts",
                dismissable=True,
                is_open=False,
                color='danger'
            )
        )
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Textarea(
                id='display_results',
                className='string_input',
                size="lg",
                readOnly=True,
                style={'font-size': '16px', 'min-height': '250px', 'max-height': '500px'}
            ),
        )
    ])
], style={"margin-bottom": '30px'})


@app.callback(
    Output('myform-external-trigger-update-internal-dict', 'children'),
    Input('show_data', 'n_clicks')
)
def update_internal_form_dict(click):
    """
    This function trigger myform internal dict update.
    When the update is done it will return a flag on
    "myform-output-update-finished-verification".
    """
    ctx = dash.callback_context

    if not ctx.triggered:
        return dash.no_update

    return str(np.random.rand())

@app.callback(
    [         
        Output('alerts', 'is_open'),
        Output('alerts', 'children'),
        Output('display_results', 'value')
    ],
    [Input('myform-output-update-finished-verification', 'children')],
    [State('alerts', 'is_open')]
)
def show_data_from_internal_dict(trigger, is_open):
    """
    This functions runs when the update internal dict is done
    It will read myform internal dict and create an output nested dict
    with the forms data, following the rules defined by the schema.
    """

    if not trigger:
        return dash.no_update

    alerts, output = my_form.data_to_nested()  # Read internal dict and get missing required fields and output nested dict

    if alerts is not None:
        return True, alerts, ''  # If any missing fields return alerts

    # Else show json data 
    json_string = json.dumps(output, indent=4)
    return False, [], json_string


if __name__ == '__main__':
    app.run_server(debug=True)
