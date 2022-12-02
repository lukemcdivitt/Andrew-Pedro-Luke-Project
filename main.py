from bs4 import BeautifulSoup
from urllib.request import urlopen

# Link to a source already with data in JSON
# https://opendata.ecdc.europa.eu/covid19/casedistribution/json/

# Link to a website that has needed data which would be more compatible with scraping

#https://www.worldometers.info/coronavirus/country/japan/
#https://www.worldometers.info/world-population/us-population/

#function can accept the website worldometers.info and country as parameters
#it then joins them to create a new link to hyperlink to specific page of that country.
#need to scrape the death toll and total population from the page.
def scrape_country (name, website):
        
    combined = website + "country/" + name
    #populationwebsite = website + "world-population/" + name + "-population"
    try:
        page = urlopen(combined)
    except:
        print("Error connecting to the URL")

    
    soup = BeautifulSoup(page, 'html.parser')
   
    
    #having an issue trying to scrape the death toll from the site.
    content = soup.findAll(('div', {"class": "news_body"}))
    stringcontent = str(content)
    x=stringcontent.find('new deaths<')
    #need to create code to extract number. x.isnumeric() is an option 
    print(stringcontent[x-3] + stringcontent[x-2])

    with open('readme.txt', 'w') as f:
        f.writelines(str(content))
    #content.find('<strong>').get_text()

scrape_country ("us", "https://www.worldometers.info/coronavirus/")