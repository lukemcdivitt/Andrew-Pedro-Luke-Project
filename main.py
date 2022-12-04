from ast import For, Str
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Link to a source already with data in JSON
# https://opendata.ecdc.europa.eu/covid19/casedistribution/json/

# Link to a website that has needed data which would be more compatible with scraping
#https://www.worldometers.info/coronavirus/country/japan/
#https://www.worldometers.info/world-population/us-population/

#function can accept the website worldometers.info and country as parameters
#it then joins them to create a new link to hyperlink to specific page of that country.
def scrape_country (name, website):
        
    countrywebsite = website + "/coronavirus/country/" + name #creates website for worldmeters.info based on country name received
    try:
        countrypage = urlopen(countrywebsite)
    except:
        print("Error connecting to the URL") 

    
    populationwebsite = website + "/world-population/" + name + "-population" #creates population website based on country name received
    try:
        populationpage = urlopen(populationwebsite)
    except:
        print("Error connecting to the URL")
    
    #code uses Beautiful soup to search website to find data phrase that is associated with the most recent total death counts.
    countrysoup = BeautifulSoup(countrypage, 'html.parser')
    countrycontent = countrysoup.findAll(('li', {"class": "news_li"}))
    stringcontent = str(countrycontent)
    x=stringcontent.find('new deaths<')
    
    #code searches back from found phrase to identify the number of most recent total deaths.
    i=2 #number starts 2 characters before 'new deaths<'
    deathlist = []
    for i in range(11): #accounts for a maximum number of less than 10 billion
        tempstr = stringcontent[x-i]
        if tempstr.isnumeric() is True:
            deathlist.append(stringcontent[x-i])
        i+=1

    strdeaths= "".join(deathlist[::-1])
    intdeaths= int(strdeaths)
    print("death count: " + strdeaths)
    
    #code uses Beautiful soup to search website to find data phrase that is associated with the most recent population of country.
    populationsoup = BeautifulSoup(populationpage, 'html.parser')
    populationcontent = populationsoup.findAll(('div', {"class": "content-inner"}))
    stringcontent = str(populationcontent)
    x=stringcontent.find('as of')
    
    #code searches back from found phrase to identify the country population
    i=12 #number starts 12 characters before 'as of'
    population = []
    for i in range(22): #accounts for a maximum country population of less than 10 billion people
        tempstr = stringcontent[x-i]
        if tempstr.isnumeric() is True:
            population.append(stringcontent[x-i])
        i+=1

    strpopulation = "".join(population[::-1])
    intpopulation=int(strpopulation)
    print(intpopulation)
    normdeaths= intdeaths/(intpopulation/1000000) #normalize data received to population per 1 million people
    print("normalized by population: " + str(normdeaths))

    with open('readme.txt', 'w') as f:
        f.writelines(str(populationcontent))
    
scrape_country ("japan", "https://www.worldometers.info")