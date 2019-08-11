from tweepy.streaming import StreamListener

class RealTimeTweetListener(StreamListener):
    """ A listener class which maintains the connection and listens for tweets
    coming from the Twitter Server and returns the tweets received.
    """
    def on_connect(self):
        pass

    def on_status(self, status):
        print "Tweet received: ", status.text.encode('utf-8')
        return status.text

    def on_error(self, status_code):
        pass

    def on_exception(self, exception):
        pass


