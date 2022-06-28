#Customizable scrapers for Twitter AND Reddit !

Selenium & Chrome Web Driver automated scrolling and scraping bot.

--- 0 ---

Requirements:
1) Python
2) An IDE of your choice (to run the .py scripts, or Jupyter Notebook to run the .ipynb)
3) Selenium Web Driver (A simple .exe file available at: https://www.selenium.dev/downloads/) *Make sure to check it's compatible with your current Chrome version.

To see full development of the bot look at the step-by-step Jupyter Notebook files in the "Trial" folders.

For fully integrated code, ready for you to use, copy the "main_scrape" scripts and costumize to your search needs accordingly. Make sure to read the commented lines as they have details on every variable you need to input.

You can choose to scrape search URLs or someone's profile directly by placing URL before the driver.get(url) funciton.

There are example in the script and #VARIABLE! tags to let you know what to change. 

You can filter by words, tags, likes, dates...

(Note: you have to add your WebDriver's PATH depending on here you installed it locally).


--- 0 ---


#Scrape the new V2 API.

Take a look at the "with_apis" script in "Twitter" => "Trial" folder.

Created to integrate Twitter's V2 API, all you need is the bearer token which can now be done in the Twitter developer's platfrom instead of in code.

Paste this code in the bearer variable for your script, of save it in ENV / .env file and call it with os or you'r method of choice for security...

Read further info for basic Query syntax for this types of requests in; https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/guides/build-standard-query

Basically: 

"space" = %20

: = %3

@ = %40

'# = %23
