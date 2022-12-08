from bokeh.models import ColorBar, ColumnDataSource, FactorRange
from bokeh.plotting import figure, show, output_file
from bokeh.transform import linear_cmap
import json

with open('Web1 7DEC22.json') as Web1:
    day1site1 = json.load(Web1)

with open('Web2 7DEC22.json') as Web2:
    day2site2 = json.load(Web2)

with open('Web2 7DEC22.json') as Web3:
    day3site3 = json.load(Web3)


output_file('index.hdml')

Countries = [day1site1[0]["Country Name"],day1site1[1]["Country Name"],day1site1[2]["Country Name"],day1site1[3]["Country Name"]]
Cases = [day1site1[0]["Cases"],day1site1[1]["Cases"],day1site1[2]["Cases"],day1site1[3]["Cases"]]
CasesNormalized = [day1site1[0]["Cases-Normalized"],day1site1[1]["Cases-Normalized"],day1site1[2]["Cases-Normalized"],day1site1[3]["Cases-Normalized"]]
Deaths = [day1site1[0]["Deaths"],day1site1[1]["Deaths"],day1site1[2]["Deaths"],day1site1[3]["Deaths"]]
DeathsNormalized = [day1site1[0]["Deaths-Normalized"],day1site1[1]["Deaths-Normalized"],day1site1[2]["Deaths-Normalized"],day1site1[3]["Deaths-Normalized"]]
Recovered = [day1site1[0]["Recovered"],day1site1[1]["Recovered"],day1site1[2]["Recovered"],day1site1[3]["Recovered"]]
RecoveredNormalized = [day1site1[0]["Recovered-Normalized"],day1site1[1]["Recovered-Normalized"],day1site1[2]["Recovered-Normalized"],day1site1[3]["Recovered-Normalized"]]
Population = [day1site1[0]["Population"],day1site1[1]["Population"],day1site1[2]["Population"],day1site1[3]["Population"]]

print(Countries)
print(Cases)
print(CasesNormalized)
print(DeathsNormalized)
print(Recovered)
print(RecoveredNormalized)
print(Population)

