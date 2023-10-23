from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__) # This creates the initializes the Dash app "object", setting it equal to the variable "app"
df = pd.read_csv("diabetes.csv")

# In this line, we are assigning the "layout" attribute of the Dash object to this html/python syntax
app.layout = html.Div([
    html.H1(children='Hello World'), # see how it is nested in the code cell below
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.RadioItems(options=['Pregnancies', 'Glucose', 'BloodPressure'], value='Pregnancies', id='my_first_selections'),
    dcc.Graph(figure={}, id='my_first_graph')
]) 

# NEW PART! This is the callback function
@callback(
    Output(component_id='my_first_graph', component_property='figure'),
    Input(component_id='my_first_selections', component_property='value')
)
def update_graph(y_col): # input -> y_col
    fig = px.histogram(df, x='Outcome', y=y_col)
    return fig # fig -> output -> figure

if __name__ == '__main__': # this is just to run the app -- this will be the same across most of your dash apps
    app.run_server(debug=True)  