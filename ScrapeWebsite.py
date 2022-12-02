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
        counters = soup.find_all('div', attrs={'class': 'maincounter-number'})

        # loop through the conatiners to find the counters
        counts = []
        for counter in counters:
            count = counter.contents[1].contents[0].replace(" ", "")
            counts.append(count)


        # convert into a dictionary
        country_info = {'country_name': country, 'Cases': counts[0], 'Deaths': counts[1], 'Recovered': counts[2]}

        # add to the large dictionary
        all_countries.append(country_info)

    # place into json
    with open('covid.json', 'w', encoding='latin-1') as f:
        json.dump(all_countries,f,indent=8,ensure_ascii=False)
    print("Mission Success!")

    # return
    return 1