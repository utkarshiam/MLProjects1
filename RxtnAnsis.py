import tweepy
import csv
from textblob import TextBlob

con_key="" ###your key
con_sec="" ###your secret

acc_token="" ###your token
acc_token_sec=""###your token secret

auth=tweepy.OAuthHandler(con_key,con_sec)
auth.set_access_token(acc_token,acc_token_sec)

api=tweepy.API(auth)
tweetTopic=input("Topic De")
bitchTweets= api.search(tweetTopic) ###add whatever topic you like

with open('dataset.csv', mode='w') as tweets_file:
	tweet_writer= csv.writer(tweets_file, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
	tweet_writer.writerow(['Tweet', 'Author','Time created', 'Sentiment' ])

	for tweet in bitchTweets:
		T_text=tweet.text
		T_user=tweet.user.name
		T_c_at=tweet.created_at
		analysis= TextBlob(tweet.text).sentiment.polarity
		print(T_text,T_user,T_c_at)
		print(analysis)
		tweet_writer.writerow([T_text, T_user,T_c_at, analysis ])
