import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import json
from pathlib import Path
from json_schema_to_dash_forms import SchemaFormContainer


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

path_source_schema = Path.cwd() / "examples_schemas/schema_source.json"

with open(path_source_schema, 'r') as inp:
    source_schema = json.load(inp)

source_form = SchemaFormContainer(
    id='sourcedata',
    schema=source_schema,
    parent_app=app
)

app.layout = dbc.Container([
    source_form,
])


if __name__ == '__main__':
    app.run_server(debug=True)