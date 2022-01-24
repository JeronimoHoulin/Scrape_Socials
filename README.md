# Tweeter_Scraper

Selenium & Chrome Web Driver automated scrolling and scraping bot.
To see full development of bot open Jupyter Notebook and read line by line. 
For fully integrated code, get the "main_scrape.py".

Here you can choose to scrape search URLs or someone's profile directly by placing URL before the driver.get(url) funciton.
There are many examples of them in the scripts, but you can paste the url from whereever in twitter you wish to scrape.


-----------------------------------------------------------  0  -----------------------------------------------------------


Scrape the new V2 API.

Created to integrate Twitter's V2 API, all you need is the bearer token which can now be done in the Twitter developer's platfrom instead of in code.

Paste this code in the bearer variable for your script, of save it in ENV / .env file and call it with os or you'r method of choice for security...

Read further info for basic Query syntax for this types of requests in; https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/build-standard-query

Basically: 

"space" = %20

: = %3

@ = %40
# = %23
 
