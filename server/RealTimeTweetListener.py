from tweepy.streaming import StreamListener

class RealTimeTweetListener(StreamListener):
    """ A listener class which maintains the connection and listens for tweets
    coming from the Twitter Server and returns the tweets received.
    """
    def on_connect(self):
        pass

    def on_status(self, status):
        print "Tweet received..."
        print status.text.encode('utf-8')
        return status.text.encode('utf-8')

    # def on_extended_tweet(self, status):
    #     try:
    #         if status is not None and status.text is not None:
    #             print "Extended Tweet Received..."
    #             extended_tweet = status['full_text']['full_text']
    #             print extended_tweet
    #             return extended_tweet
    #         else:
    #             pass
    #     except Exception:
    #         pass

    def on_error(self, status_code):
        pass

    def on_exception(self, exception):
        pass


