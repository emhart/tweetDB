import sqlite3

# create new db and make connection
conn = sqlite3.connect('ESA2014.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE tweets
             (id TEXT, user_name TEXT,screen_name TEXT, tweet_text TEXT,
              favorites INT, retweets INT, location TEXT, in_reply_to_tweet_id TEXT, in_reply_to_user_id TEXT)''')

# save (commit) the changes
conn.commit()

# close connection
conn.close()
