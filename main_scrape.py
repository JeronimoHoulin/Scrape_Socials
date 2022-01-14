#Imports
import time 
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Defining functions
def get_tweet_data(card):
    #Elements
    #GET FULL XPATH AND FOLLOW THROUGH AFTER TAG "ARTICLE"
    text = card.find_element_by_xpath('./div/div/div/div[2]/div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('./div/div/div/div[2]/div[2]/div[2]/div[2]').text
    handle = card.find_element_by_xpath('.//*[contains(text(),"@")]').text
    replies = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweets = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    likes = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    full_txt = text+responding
    
    #Sponsored tweets have no date
    try: 
        date = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException: 
        return
    
    #Create a tuple for the tweet
    tweet = (handle, full_txt, date)
    
    return tweet

#Creating an instance of a webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Making the URLs for the get function
#tweet_fields = "tweet.fields=created_at,source,text,public_metrics,author_id"
#query = "%40solana%20and%20ido%20-is%3aretweet"
#url1 = "https://twitter.com/search?query={}&{}".format(query, tweet_fields)
url1 = "https://twitter.com/search?q=%23ido%20AND%20%23solana&src=typed_query"
url3 = "https://twitter.com/search?q=%23ido%20AND%20%23solana&src=typed_query&f=live"
## Or search by Username
url2 = 'https://twitter.com/google'
driver.get(url3)
time.sleep(5)

#Create tweet ID's for already scraped tweets
tweet_ids = set()
tweet_data = []

#Check if I'm at the end of the page
last_pos = driver.execute_script("return document.body.scrollHeight")
#print(f'last post: {last_pos}')

#Set scrolilng
scrolling = True

#Looping through tweets
while scrolling:
    cards = driver.find_elements_by_css_selector("article")
    for card in cards[-15:]: 
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                tweet_data.append(tweet)
                
                
                
    scrolling_attempt = 0
    while True:
        #Finally adding pagination
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)

        #Current position and comparison to check if I'm at the bottom
        curr_pos = driver.execute_script("return document.body.scrollHeight")
        
        if last_pos == curr_pos: 
            scrolling_attempt +=1
            
            #End of scroll region
            if scrolling_attempt >= 3: 
                scrolling = False
                break
            else:
                print("Atempting to scroll again.")
                time.sleep(5)
        else:
            last_pos = curr_pos
            break
                
print(len(tweet_data))
driver.quit()