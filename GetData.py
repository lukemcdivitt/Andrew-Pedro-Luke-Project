# import
import pandas as pd

# create function to get the data
def get_data():

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

    return data1, data2, data3, d1_keys, d2_keys, d3_keys