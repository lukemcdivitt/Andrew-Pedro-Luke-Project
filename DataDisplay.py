
from bokeh.models import ColorBar, ColumnDataSource, FactorRange, CustomJS, Dropdown, CheckboxGroup
from bokeh.plotting import figure, show, output_file
from bokeh.transform import linear_cmap
from bokeh.io import show
from bokeh.layouts import column, row
from collections import OrderedDict

import pandas as pd

import json

with open('Web1 7DEC22.json') as Web1:
    day1site1 = json.load(Web1)

with open('Web2 7DEC22.json') as Web2:
    day1site2 = json.load(Web2)

with open('Web2 7DEC22.json') as Web3:
    day1site3 = json.load(Web3)


output_file('index.html')

Countries1 = []
Cases1 = []
CasesNormalized1 = []
Deaths1 = []
DeathsNormalized1 = []
Recovered1 = []
RecoveredNormalized1 = []
Population1 = []

for i in range(0,len(day1site1)):
    Countries1 += [day1site1[i]["Country Name"]]
    Cases1 += [day1site1[i]["Cases"]]
    CasesNormalized1 += [day1site1[i]["Cases-Normalized"]]
    Deaths1 += [day1site1[i]["Deaths"]]
    DeathsNormalized1 += [day1site1[i]["Deaths-Normalized"]]
    Recovered1 += [day1site1[i]["Recovered"]]
    RecoveredNormalized1 += [day1site1[i]["Recovered-Normalized"]]
    Population1 += [day1site1[i]["Population"]]

print("Website 1 Information: ")
print(Countries1)
print(Cases1)
print(CasesNormalized1)
print(DeathsNormalized1)
print(Recovered1)
print(RecoveredNormalized1)
print(Population1)




Country = []
TotalCases = []
NewCases = []
TotalDeaths = []
NewDeaths= []
TotalRecovered = []
NewRecovered = []
ActiveCases = []
SeriousCritical = []
TotCases1Mpop = []
Deaths1Mpop = []
TotalTests = []
Tests1Mpop = []
Population = []
Continent = []
CaseEveryXppl = []
DeathEveryXppl = []
TestEveryXppl = []
NewCases1Mpop = []
NewDeaths1Mpop = []
ActiveCases1Mpop = []


for i in range(0,len(day1site2)):
    Country += [day1site2[i]["Country"]]
    TotalCases += [day1site2[i]["Total Cases"]]
    NewCases += [day1site2[i]["New Cases"]]
    TotalDeaths += [day1site2[i]["New Cases"]]
    NewDeaths += [day1site2[i]["New Deaths"]]
    TotalRecovered += [day1site2[i]["Total Recovered"]]
    NewRecovered += [day1site2[i]["New Recovered"]]
    ActiveCases += [day1site2[i]["Active Cases"]]
    SeriousCritical += [day1site2[i]["Serious, Critical"]]
    TotCases1Mpop += [day1site2[i]["Tot Cases/ 1M pop"]]
    Deaths1Mpop += [day1site2[i]["Deaths/ 1M pop"]]
    TotalTests += [day1site2[i]["Total Tests"]]
    Tests1Mpop += [day1site2[i]["Tests/ 1M pop"]]
    Population += [day1site2[i]["Population"]]
    Continent += [day1site2[i]["Continent"]]
    CaseEveryXppl += [day1site2[i]["1 Case every X ppl"]]
    DeathEveryXppl += [day1site2[i]["1 Death every X ppl"]]
    TestEveryXppl += [day1site2[i]["1 Test every X ppl"]]
    NewCases1Mpop += [day1site2[i]["New Cases/ 1M pop"]]
    NewDeaths1Mpop += [day1site2[i]["New Deaths/ 1M pop"]]
    ActiveCases1Mpop += [day1site2[i]["Active Cases/ 1M pop"]]


#print("/n")
#print("Website 2 Information: ")
#print(Country)
#print(TotalCases)
#print(NewCases)
#print(TotalDeaths)
#print(NewDeaths)
#print(TotalRecovered)
#print(NewRecovered)
#print(ActiveCases)
#print(SeriousCritical)
#print(TotCases1Mpop)
#print(TotalTests)
#print(Tests1Mpop)
#print(Population)
#print(Continent)
#print(CaseEveryXppl)
#print(DeathEveryXppl)
#print(TestEveryXppl)
#print(NewCases1Mpop)
#print(ActiveCases1Mpop)

p= figure(x_range=Countries1, height=350, title="Total Deaths",
           toolbar_location=None, tools="")

p.vbar(x=Countries1, top=Deaths1, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

#show(p)

#menu = [("US"), ("India"), ("France"),("Germany"),("Brazil"),("South Korea"),("Japan"),("Italy"),("UK"),('Russia'),('Spain'),("Australia"),("Argentina"),("China"),("Netherlands"),("Iran")]

#dropdown = Dropdown(label="Country", button_type="warning", menu=menu)
#dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

#show(dropdown)

LABELS = []

for i in Countries1:
    LABELS += [i]

checkbox_group = CheckboxGroup(labels=LABELS, active=[0, 1])
checkbox_group.js_on_event('button_click', CustomJS(code="""
    console.log('checkbox_group: active=' + this.origin.active, this.toString())
"""))

show(row(checkbox_group,p))
