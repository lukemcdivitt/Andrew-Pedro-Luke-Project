# bokeh imports
from bokeh.io import show, output_notebook, push_notebook, curdoc
from bokeh.plotting import figure

from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, TabPanel, Tabs, Button
from bokeh.models.widgets import CheckboxGroup

from bokeh.layouts import column, row
from bokeh.palettes import Category20_16

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.document import document
from bokeh.models.callbacks import CustomJS
from bokeh.palettes import Category20_16

# other imports
import pandas as pd
import GetData as GD

# get the data
data1, data2, data3, d1_keys, d2_keys, d3_keys = GD.get_data()

# combine the data for the line plot
dates = [8, 9, 10]
data1_total = {}
for idx in range(len(d1_keys)):
    if idx == 0:
        data1_total[d1_keys[idx]] = data1[0][d1_keys[idx]][:].to_list()
    else:
        data1_total[d1_keys[idx]] = list()
        for idx2 in range(len(data1[1][d1_keys[idx]])):
            if idx2 > 8:
                data1_total[d1_keys[idx]].append([data1[0][d1_keys[idx]][idx2], (data1[0][d1_keys[idx]][idx2]+data1[2][d1_keys[idx]][idx2])/2, data1[2][d1_keys[idx]][idx2]])
            else:
                data1_total[d1_keys[idx]].append([data1[0][d1_keys[idx]][idx2], data1[1][d1_keys[idx]][idx2], data1[2][d1_keys[idx]][idx2]])

# combined for web2
dates = [8, 9, 10]
data2_total = {}
for idx in range(len(d2_keys)):
    if idx == 0:
        data2_total[d2_keys[idx]] = data2[0][d2_keys[idx]][:].to_list()
    else:
        data2_total[d2_keys[idx]] = list()
        for idx2 in range(len(data2[1][d2_keys[idx]])):
            data2_total[d2_keys[idx]].append([data2[0][d2_keys[idx]][idx2], data2[1][d2_keys[idx]][idx2], data2[2][d2_keys[idx]][idx2]])

#combined for web 3
dates = [8, 9, 10]
data3_total = {}
for idx in range(len(d3_keys)):
    if idx == 0:
        data3_total[d3_keys[idx]] = data3[0][d3_keys[idx]][:].to_list()
    else:
        data3_total[d3_keys[idx]] = list()
        for idx2 in range(len(data3[1][d3_keys[idx]])):
            data3_total[d3_keys[idx]].append([data3[0][d3_keys[idx]][idx2], data3[1][d3_keys[idx]][idx2], data3[2][d3_keys[idx]][idx2]])

# setup checkboxes
country_select = CheckboxGroup(labels=data1[0][d1_keys[0]][:].values.tolist(), active=[0,1])
data_select = CheckboxGroup(labels=d1_keys[1:].values.tolist(), active=[2])

# initialize for line graph


# initialize variables
country_key = [country_select.labels[idx] for idx in country_select.active]
data_key = [data_select.labels[idx] for idx in data_select.active]
country_col = d1_keys[0]
source = ColumnDataSource(data=GD.make_dataset(country_key, data1[0], data_key[0]))
print('hi')

# generate the plot
def generate_plot(source, country_key, data_key, country_col):

    # create a figure
    p = figure(height=1000, width=600, title='Statistic for Selected Countries', x_axis_label='Country', y_axis_label='Selected Value')

    # creat the barplot
    p.quad(source=source, bottom=0, top='Value', left='left', right = 'right', fill_color='color', 
        line_color='black', fill_alpha=0.75, hover_fill_alpha=0.5, hover_fill_color='navy')

    # add hover tool
    p.add_tools(HoverTool(tooltips=[('Country','@'+country_col), (list(source.data.keys())[1],'@'+list(source.data.keys())[1])]))

    return p

def generate_plot(source, country_key, data_key, country_col):

    # create a figure
    l = figure(height=1000, width=600, title='Statistic for Selected Countries', x_axis_label='Country', y_axis_label='Selected Value')

    # creat the barplot
    l.line(source=source, x=dates, y='Values')

    # add hover tool
    l.add_tools(HoverTool(tooltips=[('Country','@'+country_col), (list(source.data.keys())[1],'$y')]))

    return p

# how to update when there is a change
def update(attr, old, new):

    global legend_group
    last_active_label = list(source.data.keys())[1]

    # check which are active 
    active = [country_select.labels[idx] for idx in country_select.active]
    data_active = [data_select.labels[idx] for idx in data_select.active]
    data_act_num = data_select.active

    # find the new one
    for idx in range(len(data_active)):
        if len(data_active) > 1:
            if data_active[idx] != last_active_label:
                data_select.active = [data_act_num[idx]]
    
    data_active = [data_select.labels[idx] for idx in data_select.active]
    print(data_active)

    # create a new source
    data_key = data_active[0]
    dictionary = GD.make_dataset(active, data1[0], data_key)

    # update everything
    source.data = dictionary

# generate the intial plot
p = generate_plot(source, country_key, data_key, country_col)

# check for changes
for change in [country_select, data_select]:
    change.on_change('active', update)

# prepare the layout
country_control = column(country_select)
data_control = column(data_select)
layout = row(country_control, data_control, p)

# make tab
tab = TabPanel(child=layout, title='Website Option 1')
tabs = Tabs(tabs=[tab])
    
# show 
curdoc().add_root(tabs)
curdoc().title = "COVID Dashboard"
