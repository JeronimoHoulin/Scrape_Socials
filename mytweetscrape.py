import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "YOUR_BEARER_TOKEN_HERE"

def create_url():
    """The information that you want out of the tweet"""
    tweet_fields = "tweet.fields=created_at,source,text,public_metrics,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    """When filtering by specific query"""

    query = "%40solana%20or%20ido%20-is%3aretweet"
    "%40solana%20and%23ido"
    #Read link in the Readme.txt for standard query's in this API 
    query2 ="%23ido"

    """When looking for a specific tweet"""
    
    #ids = "ids=1473392576095006724"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&max_results={}".format(query, tweet_fields,10)
    url2 = "https://api.twitter.com/2/users/by/username/Solana?query={}&max_results={}".format(tweet_fields,10)
    url3 = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=solana&count=1"
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
