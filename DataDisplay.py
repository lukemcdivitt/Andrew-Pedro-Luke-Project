from bokeh.models import ColorBar, ColumnDataSource, FactorRange
from bokeh.plotting import figure, show, output_file
from bokeh.transform import linear_cmap
import json

with open('Web1 7DEC22.json') as Web1:
    day1site1 = json.load(Web1)

with open('Web2 7DEC22.json') as Web2:
    day1site2 = json.load(Web2)

with open('Web2 7DEC22.json') as Web3:
    day1site3 = json.load(Web3)


output_file('index.hdml')

Countries1 = []
Cases1 = []
CasesNormalized1 = []
Deaths1 = []
DeathsNormalized1 = []
Recovered1 = []
RecoveredNormalized1 = []
Population1 = []

for i in range(0,4):
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

Countries2 = []
Cases2 = []
CasesNormalized2 = []
Deaths2 = []
DeathsNormalized2 = []
Recovered2 = []
RecoveredNormalized2 = []
Population2 = []

for i in range(0,4):
    Countries2 += [day1site2[i]["Country Name"]]
    Cases2 += [day1site2[i]["Cases"]]
    CasesNormalized2 += [day1site2[i]["Cases-Normalized"]]
    Deaths2 += [day1site2[i]["Deaths"]]
    DeathsNormalized2 += [day1site2[i]["Deaths-Normalized"]]
    Recovered2 += [day1site2[i]["Recovered"]]
    RecoveredNormalized2 += [day1site2[i]["Recovered-Normalized"]]
    Population2 += [day1site2[i]["Population"]]


print("/n")
print("Website 2 Information: ")
print(Countries2)
print(Cases2)
print(CasesNormalized2)
print(DeathsNormalized2)
print(Recovered2)
print(RecoveredNormalized2)
print(Population2)

