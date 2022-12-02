# this module contains fuctions required to perform data scraping

# import libraries
import bs4
import requests
from urllib.request import urlopen
import json

# scrape country
def scrape_country(countries, website):

    # initialize dictionary
    all_countries = []

    # loop through the countries
    for country in countries:
        # setup the link
        link = website + '/country/' + country
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
        classes = ['rts-nr-int rts-nr-10e6', 'rts-nr-int rts-nr-10e3', 'rts-nr-int rts-nr-10e0']
        holder = pop_soup.find_all('div', attrs={'class': 'col-md-8 country-pop-description'})
        pop_string = holder[0].contents[0].contents[3].contents[2].contents[0].replace(" ","")
        population = float(''.join(pop_string.replace(",","")))


        # loop through the conatiners to find the counters
        counts = []
        for counter in counters:
            count = counter.contents[1].contents[0].replace(" ", "")
            count = float(count.replace(",",""))
            counts.append(count)

        # normalize the data


        # convert into a dictionary
        country_info = {'Country Name': country, 'Cases': counts[0], 'Cases-Normalized': counts[0]/population, 
        'Deaths': counts[1], 'Deaths-Normalized': counts[1]/population,
        'Recovered': counts[2], 'Recovered-Normalized': counts[2]/population}

        # add to the large dictionary
        all_countries.append(country_info)

    # place into json
    with open('covid.json', 'w', encoding='latin-1') as f:
        json.dump(all_countries,f,indent=8,ensure_ascii=False)
    print("Mission Success!")

    # return
    return 1