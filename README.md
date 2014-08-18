## `TweetDB`

A quasi user friendly method of archiving tweets using the twitter search API.It's a set of python scripts that you can easily use to create an sqlite3 database of tweets via a cronjob. This is useful because you can't get back old tweets without some $$$.  Therefore the easiest alternative is to archive them in real time. What if you don't want to program it all yourself? Well `TweetDB` is here to help.

### Requirements

  * [twython](https://github.com/ryanmcgrath/twython)
  * [sqlite3](http://www.sqlite.org/) *You have this already on a mac most likely*
  * [Twitter API access using OAuth2](http://themebeans.com/how-to-create-access-tokens-for-twitter-api-1-1/)

### Getting started

Start by cloning the repo to your local machine.

```bash
git clone https://github.com/emhart/tweetDB.git
```

First to access Twitter you'll need to get your App Key and App Secret. To keep these protected I store them in a separate text file.  It's called credentials.txt.  You'll first have to edit that file.

The workhorse of this function is `tweetDB.sh`, a bash shell script that will create an SQLite3 database, and search for your twitter results. Usage is:
```bash
bash tweetDB.sh <databaseName> <searchString>
```
This will create a database with the given name, search for your search string and store all results in a table called 'tweets'

So if you want to search for tweets from the annual Ecological Society of America meeting simply use the following
```bash
bash tweetDB.sh ESA2014 "#ESA2014"
```
That will create a database called ESA2014, and store all results for the hashtag.  Because hashtags use the '#' symbol, these searches need to be in quotes.

### Archiving

If you want to archive tweets over the course of a meeting or other specific time period this is easily done with a [cron job](http://www.thesitewizard.com/general/set-cron-job.shtml).  Simply edit your crontab file with `crontab -e`.  To archive tweets from the ESA2014 meeting I used the following script crontab.

```bash
00 07-20 * * * /home/NEON/thart/tweetDB/tweetDB.sh ESA2014 "#ESA2014"
```
This ran the search every hour between 7 am and 8 pm.

So now you can easily archive any meeting hashtag for your own analysis later on at your convenience.

Happy twitter archiving.
