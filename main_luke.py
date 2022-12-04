# this is a test main file written by luke

# imports
import ScrapeWebsite as SW

# initialize test cases
# website = 1 is https://www.worldometers.info/coronavirus (finds limited information for particular countries)
# website = 2 returns information from all countries in https://www.worldometers.info/coronavirus/#countries
# website = 3 returns all information provided by 'https://covid19.who.int/table'

website = 1
country = ['japan', 'us', 'germany', 'china']
filename = 'test3.json'

# run the test case
SW.scrape_country(website, filename, country)

