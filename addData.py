import sqlite3
import twitterSearch as tS
import re

# make connection to existing db
conn = sqlite3.connect('ESA2014.db')
cur = conn.cursor()
myData = tS.twitter_search("#ESA2014")
toWrite = tS.dbTuple(myData)

### Grab all ID's from the DB and make sure there are no duplicates

conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT id FROM tweets")

rows = cur.fetchall()
idList = [row[0] for row in rows]
idList = " ".join(idList)

### Make copy of data that you can pop entries from
toWriteCopy = list(toWrite)
for entry in toWriteCopy:
     if re.search(entry[0], idList):
          toWrite.remove(entry)


cur.executemany('INSERT INTO tweets VALUES (?,?,?,?,?,?,?,?,?,?)', toWrite)

    # save changes
conn.commit()


# close connection
conn.close()
