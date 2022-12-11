# bokeh imports
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.models import HoverTool
from bokeh.models.widgets import CheckboxGroup
from bokeh.models import ColumnDataSource

# other imports
import pandas as pd

# generate a figure
def generate_figure(x_values, title, x_label, y_label):
    p = figure(height=600, width=1000, x_range=x_values, title=title, x_axis_label=x_label, y_axis_label=y_label)
    return p

# generate bar plot
def bar_plot(source, country_key, data_key, title, x_label, y_label, countries):
    p = generate_figure(countries, title, x_label, y_label)
    p.vbar(x=country_key, source=source, top=data_key, fill_color='red', line_color='black', fill_alpha=0.75, hover_fill_alpha=1.0, hover_fill_color='navy')
    p.add_tools(HoverTool(tooltips=[('Country',"@Country_Name"), ('Value', "@Cases")]))
    return p

# make the dataset for interactions
def make_dataset(countries, dataframe):

    # get info on the dataframe
    keys = dataframe.keys()

    # set up new dataframe
    interested = pd.DataFrame(columns=keys)

    # get the desired coutries
    for idx, row in enumerate(dataframe):
        if any(row == countries[idx]):
            interested.append(row)

    return ColumnDataSource(interested)
