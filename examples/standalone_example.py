import dash
import dash_bootstrap_components as dbc
import json
from pathlib import Path
from json_schema_to_dash_forms import SchemaFormContainer


external_stylesheets = [dbc.themes.BOOTSTRAP]
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
    my_form,
])


if __name__ == '__main__':
    app.run_server(debug=True)
