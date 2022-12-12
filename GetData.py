# import
import pandas as pd

from bokeh.palettes import Category20_16

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

    for keys in d1_keys:
        data1 = [data.rename(columns={keys:keys.replace('-','_')}) for data in data1]
    for keys in d2_keys:
        data2 = [data.rename(columns={keys:keys.replace('-','_')}) for data in data2]
    for keys in d3_keys:
        data3 = [data.rename(columns={keys:keys.replace('-','_')}) for data in data3]

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

# function to create a new dataset
def make_dataset(countries, dataframe, data_key):

    # get info on the dataframe
    keys = dataframe.keys()

    # set up new dataframe
    interested = pd.DataFrame(columns=[keys[0], data_key])

    # get the desired coutries
    for idx in range(len(dataframe)):
        for idx2 in range(len(countries)):
            for idx3 in range(len(dataframe.loc[idx])):
                if dataframe.loc[idx][idx3] == countries[idx2]:
                    interested = interested.append(dataframe.loc[idx,[keys[0],data_key]])

    interested = interested.rename(columns={data_key: 'Value'})
    # convert to dictinary
    sub_dict = {}
    for key in [keys[0], 'Value']:
        sub_dict[key] = interested[key].to_list()
    sub_dict['left'] = [-1] * len(sub_dict[keys[0]])
    sub_dict['right'] = [1] * len(sub_dict[keys[0]])
    sub_dict['color'] = [1] * len(sub_dict[keys[0]])

    for idx in range(len(sub_dict[keys[0]])):
        sub_dict['color'][idx] = Category20_16[idx]

    for idx in range(len(sub_dict['Value'])):
        try:
            sub_dict['Value'][idx] = int(sub_dict['Value'][idx])
        except:
            sub_dict['Value'][idx] = int(sub_dict['Value'][idx].replace(' ','').replace(',',''))

    return sub_dict

# line graph
def make_dataset_line(countries, dictionary, data_key):

    sub_dict = {}
    keys = list(dictionary.keys())
    dates = [8, 9, 10]
    sub_dict[keys[0]] = []
    sub_dict['Value'] = []
    sub_dict['Dates'] = []
    sub_dict['Color'] = []
    color = 0

    for idx in range(len(dictionary[keys[0]])):
        for country2 in countries:
            if dictionary[keys[0]][idx] == country2:
                sub_dict[keys[0]].append(dictionary[keys[0]][idx])
                sub_dict['Value'].append(dictionary[data_key][idx])
                sub_dict['Dates'].append(dates)
                if idx > len(Category20_16):
                    sub_dict['Color'].append(Category20_16[color])
                else:
                    sub_dict['Color'].append(Category20_16[color])
                color +=1

    return sub_dict