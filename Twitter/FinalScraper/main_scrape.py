
"""For the times when you only need new tweets
    a.k.a limit the timeframe with before_date."""
"""Imports"""
import time 
from selenium import webdriver
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


#Creating an instance of a webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


""" Variables """

#url = "https://twitter.com/search?q=%23ido%20AND%20%23solana&src=typed_query"
#url = "https://twitter.com/search?q=solana%20AND%20funding&src=typed_query&f=live"

username = "Solana_Nation"

## Or search by Username
url = f'https://twitter.com/{username}'

#Set other parameters:
stringys = ["fund", "seed", "private", "upcoming", "ido", "Hiring"]
before_date = datetime(2022, 2, 10)

#GENERATE THE REQUEST !
driver.get(url)

#wait till load
time.sleep(30)
print("Page ready !")

#Create tweet ID's for already scraped tweets
tweet_ids = set()
tweet_data = []

#Check if I'm at the end of the page
last_pos = driver.execute_script("return document.body.scrollHeight")
#print(f'last post: {last_pos}')

#Set scrolilng
scrolling = True
in_range = True

#Looping through tweets
while scrolling:
    #Define the tweet segment
    cards = driver.find_elements_by_css_selector("article")
    
    for card in cards: 
        
        """ Function """
        try:
            #Elements
            #GET FULL XPATH AND FOLLOW THROUGH AFTER TAG "ARTICLE" 
            text = card.find_element_by_xpath('./div/div/div/div[2]/div[2]/div[2]/div[1]').text
            responding = card.find_element_by_xpath('./div/div/div/div[2]/div[2]/div[2]/div[2]').text
            handle = card.find_element_by_xpath('.//*[contains(text(),"@")]').text
            #replies = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
            #retweets = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
            #likes = card.find_element_by_xpath('.//div[@data-testid="like"]').text
            #pinned = card.find_element_by_xpath('./div/div/div/div[1]/div/div/div/div/div[2]/div/div/div').text
            full_txt = text+responding
            
            #Sponsored tweets have no date
            date = card.find_element_by_xpath('.//time').get_attribute('datetime')

            """STR date into python datetime object"""
            #date = date.rstrip(".000Z")
            date = date[:-5]
            date = date.replace("T", " ")
            date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            #print(date_obj)
            
        #NoSuchElement error handling
        except NoSuchElementException:
            pass
        #StaleElementReferenceException error handling
        except StaleElementReferenceException:
            pass
        
        if any(s in text.lower() for s in stringys):
        
            if date_obj > before_date:
                #Create a tuple for the tweet
                tweet = (handle, date, full_txt)

                #Create the tweet DF
                tweet_id = ''.join(tweet)

                #Add only tweets not already seen
                if tweet_id not in tweet_ids:
                    #Add id & data
                    tweet_ids.add(tweet_id)
                    tweet_data.append(tweet)
            """       
            #This makes the bot skip pinned tweets; Because they have dates which are late...
            if "Tweet fijado".lower() in pinned.lower():
                if stringy in text:
                    #Create a tuple for the tweet
                    tweet = (handle, date, full_txt)

                    #Create the tweet DF
                    tweet_id = ''.join(tweet)

                    #Add only tweets not already seen
                    if tweet_id not in tweet_ids:
                        #Add id & data
                        tweet_ids.add(tweet_id)
                        tweet_data.append(tweet)
            """
        if date_obj < before_date:
            scrolling = False
            in_range = False
            print("tweet out of range")
            break

            
    scrolling_attempt = 0
    
    while in_range == True:
        #Finally adding pagination
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)

        #Current position and comparison to check if I'm at the bottom
        curr_pos = driver.execute_script("return document.body.scrollHeight")
        
        if last_pos == curr_pos: 
            #If I scrolled and ended up in the same place //nothing loaded//
            scrolling_attempt +=1
            
            #End of scroll region
            if scrolling_attempt >= 3: 
                scrolling = False
                break
            else:
                print(f'{scrolling_attempt}^st Attempt to scroll. Break in 3rd.')
                time.sleep(10)
        else:
            last_pos = curr_pos
            break
    else:
        break
                
"""Results"""
print("---------------------------------------------------")
print(f'Amount of tweets collected: {len(tweet_data)}')
print("---------------------------------------------------")
for i in tweet_data: 
    print("---------0---------")
    print(i)

driver.quit()
