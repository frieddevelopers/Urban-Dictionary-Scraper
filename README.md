# Urban-Dictionary-Scraper
This project is a web scraper which scrapes Urban Dictionary using scrapy. 
If you don't have scrapy, you can install with pip install scrapy.
To run go into urban/urban folder and run "scrapy crawl urban_scraper".
If you want the headers to change on every request, then change lines 18 - 23 with API_KEY = "Your scrapeops api key".
The program then saves the scraped data to a file called words.json in the urban folder.
