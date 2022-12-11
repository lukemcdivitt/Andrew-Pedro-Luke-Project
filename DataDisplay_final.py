# bokeh imports
from bokeh.io import show, output_notebook, push_notebook, curdoc
from bokeh.plotting import figure

from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, TabPanel, Tabs
from bokeh.models.widgets import CheckboxGroup

from bokeh.layouts import column, row
from bokeh.palettes import Category20_16

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.document import document
from bokeh.models.callbacks import CustomJS

# other imports
import pandas as pd
from GetData import get_data

# function to create a new dataset
def make_dataset(countries, dataframe):

    # get info on the dataframe
    keys = dataframe.keys()

    # set up new dataframe
    interested = pd.DataFrame(columns=keys)

    # get the desired coutries
    for idx in range(len(dataframe)):
        for idx2 in range(len(countries)):
            for idx3 in range(len(dataframe.loc[idx])):
                if dataframe.loc[idx][idx3] == countries[idx2]:
                    interested = interested.append(dataframe.loc[idx])

    return interested

# function to generate the plot
def generate_plot(source, country_key, data_key, country_col):

    # create a figure
    p = figure(height=600, width=1000, x_range=country_key, title='Number for Selected Countries', x_axis_label='Country', y_axis_label=data_key)

    # creat the barplot
    p.vbar(source=source, top=data_key, x=country_col, fill_color='red', line_color='black', fill_alpha=0.75, hover_fill_alpha=1.0, hover_fill_color='navy')

    # add hover tool
    p.add_tools(HoverTool(tooltips=[('Country','@'+country_col), (data_key,'@'+data_key)]))

    return p

# how to update when there is a change
def update(attr, old, new):

    # verify that only one data box is ticked
    new_ticks = data_select.active
    if len(new_ticks) > 1:
        data_select.active = current_ticks
    else:
        current_ticks = data_select.active

    # check which are active 
    active = [country_select.labels[idx] for idx in country_select.active]
    data_active = data_select.labels

    # create a new source
    dataframe = make_dataset(active, data1)
    new_source = ColumnDataSource(dataframe)
    country_key = dataframe.keys()[0]
    data_key = data_active

    # update everything
    source.data.update(new_source.data)

# get the data
data1, data2, data3, d1_keys, d2_keys, d3_keys = get_data()

country_select = CheckboxGroup(labels=data1[0][d1_keys[0]][:].values.tolist(), active=[0,1])
country_select.on_change('active', update)

data_select = CheckboxGroup(labels=d1_keys[1:].values.tolist(), active=[0,1])
data_select.on_change('active', update)

country_control = column(country_select)
data_control = column(data_select)

country_key = [country_select.labels[idx] for idx in country_select.active]
#data_select.active = [d1_keys[1]]
data_key = d1_keys[1]

source = ColumnDataSource(make_dataset(country_key, data1[0]))
country_col = d1_keys[0]

p = generate_plot(source, country_key, data_key, country_col)

layout = row(country_control, data_control, p)

# make tab
tab = TabPanel(child=layout, title='COVID Dashboard')
tabs = Tabs(tabs=[tab])
    
# show 
show(tabs)
