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
from bokeh.palettes import Category20_16, Iridescent

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
        for idx2 in range(len(data1[0][d1_keys[0]])):
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
country_select = CheckboxGroup(labels=data1[0][d1_keys[0]][:].values.tolist(), active=[0,1]) #1
data_select = CheckboxGroup(labels=d1_keys[1:].values.tolist(), active=[2]) #1
country_select_2 = CheckboxGroup(labels=data2[0][d2_keys[0]][:].values.tolist(), active=[0,1]) #1
data_select_2 = CheckboxGroup(labels=d2_keys[1:].values.tolist(), active=[2]) #1
country_select_3 = CheckboxGroup(labels=data3[0][d3_keys[0]][:].values.tolist(), active=[0,1]) #1
data_select_3 = CheckboxGroup(labels=d3_keys[1:].values.tolist(), active=[2]) #1

# initialize variables
country_key = [country_select.labels[idx] for idx in country_select.active]
data_key = [data_select.labels[idx] for idx in data_select.active]
country_col = d1_keys[0]
source = ColumnDataSource(data=GD.make_dataset(country_key, data1[0], data_key[0]))

# initialize for line graph
line_country_select = GD.make_dataset_line(country_key, data1_total, data_key[0])
source_line = ColumnDataSource(data=line_country_select)

# for tab 2
country_key_2 = [country_select_2.labels[idx] for idx in country_select_2.active]
data_key_2 = [data_select_2.labels[idx] for idx in data_select_2.active]
country_col_2 = d2_keys[0]
source_2 = ColumnDataSource(data=GD.make_dataset(country_key_2, data2[0], data_key_2[0]))
line_country_select_2 = GD.make_dataset_line(country_key_2, data2_total, data_key_2[0])
source_line_2 = ColumnDataSource(data=line_country_select_2)

# for tab 3
country_key_3 = [country_select_3.labels[idx] for idx in country_select_3.active]
data_key_3 = [data_select_3.labels[idx] for idx in data_select_3.active]
country_col_3 = d3_keys[0]
source_3 = ColumnDataSource(data=GD.make_dataset(country_key_3, data3[0], data_key_3[0]))
line_country_select_3 = GD.make_dataset_line(country_key_3, data3_total, data_key_3[0])
source_line_3 = ColumnDataSource(data=line_country_select_3)

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

def generate_plot_line(source_line, country_key, data_key, country_col):

    # create a figure
    l = figure(height=600, width=500, title='Statistic for Selected Countries Over Three Days', x_axis_label='Country', y_axis_label='Selected Value')

    # creat the barplot
    l.multi_line(source=source_line, xs='Dates', ys='Value')

    # add hover tool
    l.add_tools(HoverTool(tooltips=[('Country','@'+country_col), (list(source.data.keys())[1],'$y')]))

    return l

# how to update 1 when there is a change
def update(attr, old, new):

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
    dict_line = GD.make_dataset_line(active, data1_total, data_key)

    # update everything
    source.data = dictionary
    source_line.data = dict_line

# how to update 2 when there is a change
def update_2(attr, old, new):

    last_active_label_2 = list(source_2.data.keys())[1]

    # check which are active 
    active_2 = [country_select_2.labels[idx] for idx in country_select_2.active]
    data_active_2 = [data_select_2.labels[idx] for idx in data_select_2.active]
    data_act_num_2 = data_select_2.active

    # find the new one
    for idx in range(len(data_active_2)):
        if len(data_active_2) > 1:
            if data_active_2[idx] != last_active_label_2:
                data_select_2.active = [data_act_num_2[idx]]
    
    data_active_2 = [data_select_2.labels[idx] for idx in data_select_2.active]
    print(data_active_2)

    # create a new source
    data_key_2 = data_active_2[0]
    dictionary_2 = GD.make_dataset(active_2, data2[0], data_key_2)
    dict_line_2 = GD.make_dataset_line(active_2, data2_total, data_key_2)

    # update everything
    source_2.data = dictionary_2
    source_line_2.data = dict_line_2

# how to update 3 when there is a change
def update_3(attr, old, new):

    last_active_label_3 = list(source_3.data.keys())[1]

    # check which are active 
    active_3 = [country_select_3.labels[idx] for idx in country_select_3.active]
    data_active_3 = [data_select_3.labels[idx] for idx in data_select_3.active]
    data_act_num_3 = data_select_3.active

    # find the new one
    for idx in range(len(data_active_3)):
        if len(data_active_3) > 1:
            if data_active_3[idx] != last_active_label_3:
                data_select_3.active = [data_act_num_3[idx]]
    
    data_active_3 = [data_select_3.labels[idx] for idx in data_select_3.active]
    print(data_active_3)

    # create a new source
    data_key_3 = data_active_3[0]
    dictionary_3 = GD.make_dataset(active_3, data3[0], data_key_3)
    dict_line_3 = GD.make_dataset_line(active_3, data3_total, data_key_3)

    # update everything
    source_3.data = dictionary_3
    source_line_3.data = dict_line_3

# generate the intial plot
p = generate_plot(source, country_key, data_key, country_col)
l = generate_plot_line(source_line, country_key, data_key, country_col)
p_2 = generate_plot(source_2, country_key_2, data_key_2, country_col_2)
l_2 = generate_plot_line(source_line_2, country_key_2, data_key_2, country_col_2)
p_3 = generate_plot(source_3, country_key_3, data_key_3, country_col_3)
l_3 = generate_plot_line(source_line_3, country_key_3, data_key_3, country_col_3)

# check for changes
for change in [country_select, data_select]:
    change.on_change('active', update)
for change_2 in [country_select_2, data_select_2]:
    change_2.on_change('active', update_2)
for change_3 in [country_select_3, data_select_3]:
    change_3.on_change('active', update_3)

# prepare the layout
country_control = column(country_select)
data_control = column(data_select)
layout = row(country_control, data_control, p,l)
country_control_2 = column(country_select_2)
data_control_2 = column(data_select_2)
layout_2 = row(country_control_2, data_control_2, p_2,l_2)
country_control_3 = column(country_select_3)
data_control_3 = column(data_select_3)
layout_3 = row(country_control_3, data_control_3, p_3,l_3)

# make tab
tab = TabPanel(child=layout, title='Website Option 1')
tab_2 = TabPanel(child=layout_2, title='Website Option 2')
tab_3 = TabPanel(child=layout_3, title='Website Option 3')
tabs = Tabs(tabs=[tab, tab_2, tab_3])
    
# show 
curdoc().add_root(tabs)
curdoc().title = "COVID Dashboard"
