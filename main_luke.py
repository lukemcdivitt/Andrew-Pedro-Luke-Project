# this is a test main file written by luke

# imports
import ScrapeWebsite as SW

# initialize test cases
# website = 1 is https://www.worldometers.info/coronavirus (finds limited information for particular countries)
# website = 2 returns information from all countries in https://www.worldometers.info/coronavirus/#countries
# website = 3 returns all information provided by 'https://covid19.who.int/table'

website = 1
country = ['japan', 'us', 'germany', 'china']
filename = 'test1 2nd day.json'

# run test case for website 1
SW.scrape_country(website, filename, country)

website = 2
filename = 'test2 2nd day.json'
# run test case for website 2
SW.scrape_country(website, filename, country)

website = 3
filename = 'test3 2nd day.json'
#creates data file for website 3
SW.scrape_country(website, filename, country)
