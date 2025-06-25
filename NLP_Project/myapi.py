import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key()

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response
