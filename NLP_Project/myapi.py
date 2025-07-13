import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key("YOUR_API_KEY_HERE")

    def sentiment_analysis(self, text):
        try:
            response = paralleldots.sentiment(text)
            if 'sentiment' in response:
                return response['sentiment']
            else:
                return {"error": "Invalid response from Sentiment API"}
        except Exception as e:
            return {"error": str(e)}

    def ner(self, text):
        try:
            response = paralleldots.ner(text)
            if 'entities' in response:
                return response['entities']
            else:
                return {"error": "Invalid response from NER API"}
        except Exception as e:
            return {"error": str(e)}

    def emotion_prediction(self, text):
        try:
            response = paralleldots.emotion(text)
            if 'emotion' in response:
                return response['emotion']
            else:
                return {"error": "Invalid response from Emotion API"}
        except Exception as e:
            return {"error": str(e)}
