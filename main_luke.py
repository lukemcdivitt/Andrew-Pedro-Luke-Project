# this is a test main file written by luke

# imports
import ScrapeWebsite as SW

# initialize test cases
website = 'https://www.worldometers.info/coronavirus'
country = ['japan', 'us', 'germany', 'china']

# run the test case
SW.scrape_country(country, website)

