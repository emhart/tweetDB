from twython import Twython
#import numpy as np


APP_KEY = '4h7uwdRNPeFQ8ojddWzZQ'
APP_SECRET = '4AXOp4c8CM6T9wT1zWXydsA1yc2lWk8RvFgK7V85qU0'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

def twitter_search(term,mycount = 100):

    '''
    Simple function to search the twitter api using cursor method documented in: https://dev.twitter.com/docs/working-with-timelines

    Param
    -------
    term: string
    the string you want to search for

    myCount: int
    the number of results per page, limited to 100

    Returns
    ---------
    searches
    A list of twitter searches.

    '''

    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    searches = []
    searches.append(twitter.search(q = term,count = mycount))


    if len(searches[0]['statuses']) < mycount:
        return(searches)

    else:
        max_id = searches[0]['statuses'][(mycount-1)]['id'] - 1
        x = 1
        while x < 100:
            searches.append(twitter.search(q = term, count = mycount, max_id=max_id))
            mycount = min([mycount,len(searches[x]['statuses'])])
            if mycount < 5:
                break
            max_id = searches[x]['statuses'][(mycount - 1)]['id'] - 1
            x += 1
    return(searches)

def dbTuple(twittersearch):
    '''
    This will create a list of tuples that match the form of the database created in createDB.py
    :param twittersearch: a twython twitter search results dictionary from twitter_search()
    :return: a list of tuples from the search results
    '''
    dbtuples = []
    for i in twittersearch:
        for j in i['statuses']:
            entry = (j["id_str"],j["user"]['name'].encode('ascii','ignore'),j['user']['screen_name'].encode('ascii','ignore'),j['text'],j["favorite_count"],
            j['retweet_count'], j['geo'],j['in_reply_to_status_id_str'],j['in_reply_to_user_id'])

        dbtuples.append(entry)
    return(dbtuples)
