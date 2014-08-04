import sqlite3
import twitterSearch as tS

# make connection to existing db
conn = sqlite3.connect('ESA2014.db')
cur = conn.cursor()
myData = tS.twitter_search("#ESA2014",mycount=5)
toWrite = tS.dbTuple(myData)
print len(toWrite)
cur.executemany('INSERT INTO tweets VALUES (?,?,?,?,?,?,?,?,?)', toWrite)

    # save changes
conn.commit()

# print column names
cur.execute("SELECT * FROM tweets")
col_name_list = [tup[0] for tup in cur.description]
print col_name_list

# close connection
conn.close()
