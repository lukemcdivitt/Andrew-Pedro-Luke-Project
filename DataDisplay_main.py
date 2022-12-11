# bokeh imports
from bokeh.io import show, output_notebook, push_notebook
from bokeh.plotting import figure

from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, TabPanel, Tabs
from bokeh.models.widgets import CheckboxGroup

from bokeh.layouts import column, row
from bokeh.palettes import Category20_16

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application

# other imports
import pandas as pd
import DataDisplay_Functions as DDF

# report the date recorded
days = ['8', '9', '10']

# setup lists to hold all of the data for each day
data1 = []
data2 = []
data3 = []

# read in the data from the jsons
for idx in range(len(days)):

    # add the data form each day into new dataframe within the list
    data1.append(pd.read_json(days[idx] + 'DEC22site1.json',encoding='latin-1'))
    data2.append(pd.read_json(days[idx] + 'DEC22site2.json',encoding='latin-1'))
    data3.append(pd.read_json(days[idx] + 'DEC22site3.json',encoding='latin-1'))

# fix the title
data1 = [data.rename(columns={'Country Name': 'Country_Name'}) for data in data1]

# record the keys for each set of data
d1_keys = data1[0].keys()
d2_keys = data2[0].keys()
d3_keys = data3[0].keys()

# record all of the countries for each website for each day
country_1 = []
country_2 = []
country_3 = []

for idx in range(len(days)):

    country_1.append(data1[idx][d1_keys[0]])
    country_2.append(data2[idx][d2_keys[0]])
    country_3.append(data3[idx][d3_keys[0]])

# convert to column data source
data1_cs = [ColumnDataSource(data) for data in data1]
data2_cs = [ColumnDataSource(data) for data in data2]
data3_cs = [ColumnDataSource(data) for data in data3]

# generate a plot
title = 'test'
xlabel = 'x'
ylabel = 'y'
src = data1_cs[0]
p = DDF.bar_plot(src, d1_keys[0], d1_keys[1], title, xlabel, ylabel, data1[0][d1_keys[0]])

# create the check boxes
country_selection = CheckboxGroup(labels=country_1[0].values.tolist(), active=[0,1])

# find the correct countries to plot
def update(attr, old, new):

    # get the active
    active = [country_selection.labels[idx] for idx in country_selection.active]

    # generate the new dataset
    new_src = DDF.make_dataset(active)

    # update the source in the graph
    src.data.update(new_src.data)

# link the change
country_selection.on_change('active', update)

# put controls together
controls = column(country_selection)

# create layout
layout = row(controls,p)

# make tab
tab = TabPanel(child=layout, title='COVID Dashboard')
tabs = Tabs(tabs=[tab])

# show the plot
show(tabs)

print('dine')
