import sqlite3
import sys
import os
# create new db and make connection
dbname = sys.argv[1]


if not os.path.isfile(dbname):
  conn = sqlite3.connect(dbname)

  c = conn.cursor()

  # create table
  c.execute('''CREATE TABLE tweets
               (id TEXT, created_at TEXT ,user_name TEXT,screen_name TEXT, tweet_text TEXT,
                favorites INT, retweets INT, location TEXT, in_reply_to_tweet_id TEXT, in_reply_to_user_id TEXT)''')

  # save (commit) the changes
  conn.commit()

  # close connection
  conn.close()
