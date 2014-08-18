import sqlite3
import twitterSearch as tS
import re
import sys

dbname = sys.argv[1]
hashtag = sys.argv[2]

# make connection to existing db
conn = sqlite3.connect(dbname)
cur = conn.cursor()
myData = tS.twitter_search(hashtag)
toWrite = tS.dbTuple(myData)

### Grab all ID's from the DB and make sure there are no duplicates

conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT id FROM tweets")

rows = cur.fetchall()
idList = [row[0] for row in rows]
idList = " ".join(idList)

### Make copy of data that you can pop entries from
### This makes sure you have no duplicates
toWriteCopy = list(toWrite)
for entry in toWriteCopy:
     if re.search(entry[0], idList):
          toWrite.remove(entry)

print("Adding " + str(len(toWrite)) + " new records to your database")

cur.executemany('INSERT INTO tweets VALUES (?,?,?,?,?,?,?,?,?,?)', toWrite)

    # save changes
conn.commit()


# close connection
conn.close()
