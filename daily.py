#!/usr/bin/python

import mechanize
import re
import twitter
import oauth.oauth
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('params.ini')

consumer_key = config.get('twitter', 'consumer_key')
consumer_secret = config.get('twitter', 'consumer_secret')
access_token_key = config.get('twitter', 'access_token_key')
access_token_secret = config.get('twitter', 'access_token_secret')

br = mechanize.Browser()
response = br.open("http://www.pedroandvinnys.com/time.html")
assert br.viewing_html()
body = response.read()

below = '<!--John\sChange\sBelow\sThis\sline\sonly\**\s-->'
above = '<!--John\sChange\sAbove\sThis\sline\sonly\**\s-->'

below = re.search( below, body )
above = re.search( above, body )

start = below.end()
end = above.start()

update = body[start:end]

status = update.strip()

if len(status) <= 124:
    status = status + ' #pedroandvinnys'

if len(status) <= 131:
    status = status + ' #burrito'

api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

print api.PostUpdate(status)
