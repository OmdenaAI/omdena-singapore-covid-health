#import files and give access to tokens and keys
import tweepy,json
import os
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


#Create a file to save all tweets in it 
tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweet.txt","w")
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<1000:
            return True
        else:
            return False
        self.file.close()


#Below is a filter that extract tweets based on the keywords 

#create streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth,l)

#this line filters twiiter streams to capture data by keywords
stream.filter(track=['covid','corona','covid19','coronavirus', 'facemask','sanitizer','social-distancing'])

