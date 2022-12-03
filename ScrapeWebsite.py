# this module contains fuctions required to perform data scraping

# import libraries
import bs4
import requests
from urllib.request import urlopen
import json

# scrape country
# accepts a list input of countries to be scraped
# website is the base website to be scraped
def scrape_country(countries, website, filename):

    # initialize dictionary
    all_countries = []

    # choose website
    if website == 1:

        # loop through the countries
        for country in countries:
        # setup the link
            link = 'https://www.worldometers.info/coronavirus' + '/country/' + country
            pop_link = 'https://www.worldometers.info/world-population/' + country + '-population/'

            # establish connection with website
            try:
                page = urlopen(link)
            except:
                print("Error connecting to the URL")

            # establish connection with population website
            try:
                page = urlopen(pop_link)
            except:
                print("Error connecting to the URL")

            # get response object
            response = requests.get(link)
            pop_response = requests.get(pop_link)

            # create the parsed tree with soup
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            pop_soup = bs4.BeautifulSoup(pop_response.text,"html.parser")

            # find all the div's
            counters = soup.find_all('div', attrs={'class': 'maincounter-number'})
        
            # find the population
            holder = pop_soup.find_all('div', attrs={'class': 'col-md-8 country-pop-description'})
            pop_string = holder[0].contents[0].contents[3].contents[2].contents[0].replace(" ","")
            population = float(''.join(pop_string.replace(",","")))

            # loop through the conatiners to find the counters
            counts = []
            for counter in counters:
                count = counter.contents[1].contents[0].replace(" ", "")
                count = float(count.replace(",",""))
                counts.append(count)

            # normaliztaion number
            norm = 1000000.0

            # convert into a dictionary
            country_info = {'Country Name': country, 'Cases': counts[0], 'Cases-Normalized': counts[0]/population, 
            'Deaths': counts[1], 'Deaths-Normalized': counts[1]/population,
            'Recovered': counts[2], 'Recovered-Normalized': counts[2]/population,
            'Population': population}

            # add to the large dictionary
            all_countries.append(country_info)

    elif website == 2:

        # setup the link
        link = 'https://www.worldometers.info/coronavirus/#countries'

        # establish connection with website
        try:
            page = urlopen(link)
        except:
            print("Error connecting to the URL")

        # get response object
        response = requests.get(link)

        # create the parsed tree with soup
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # find all the div's
        rows = soup.find_all('tr', attrs={'style': ""})

        # loop through the rows and record the values
        table = []
        for row in rows:
            info = []
            for idx in range(len(row)):
                if hasattr(row.contents[idx], 'contents'):
                    if row.contents[idx] != '\n':
                        if len(row.contents[idx].contents) > 0:
                            info.append(row.contents[idx].contents[0])
                        else:
                            info.append('NA')
            table.append(info)

        # fix the data
        for idx in range(len(table)):
            for idx_cell in range(len(table[idx])):
                if hasattr(table[idx][idx_cell],'contents'):
                    table[idx][idx_cell] = table[idx][idx_cell].contents[0]

        # declare the variables
        variables = ['Country', 'Total Cases', 'New Cases', 'Total Deaths',
        'New Deaths', 'Total Recovered', 'New Recovered', 'Active Cases', 
        'Serious, Critical', 'Tot Cases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests',
        'Tests/ 1M pop', 'Population', 'Continent', '1 Case every X ppl', '1 Death every X ppl',
        '1 Test every X ppl', 'New Cases/ 1M pop', 'New Deaths/ 1M pop', 
        'Active Cases/ 1M pop']

        # set up the dictionary
        for idx in range(2,len(table)):
            country_dict = {}
            for idx_cell in range(1,len(table[idx])):
                country_dict.update({variables[idx_cell-1]: table[idx][idx_cell]})
            all_countries.append(country_dict)

    elif website == 3:

        # begin 3rd method (2nd website)
        

    # place into json
    with open(filename, 'w', encoding='latin-1') as f:
        json.dump(all_countries,f,indent=8,ensure_ascii=False)
    print("Mission Success!")

    # return
    return 1