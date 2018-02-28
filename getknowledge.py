import requests

class GetKnowledge:
    def __init__(self):
        self.url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/e6c50e57-a4f3-4650-a05b-9498684f4869?subscription-key=58606e5abb7d4613bebdf1ac3ef328a8&verbose=true&timezoneOffset=330&q="
        pass
    def get_intent(self, query):
        # attaching query
        URL = self.url + query
        #making  API request to the LUIS framework
        r = requests.get(URL,verify = False)

        #getting the response json
        resultLUIS = r.json()
        #extracting the intent and the intent score from the json
        topScoringIntent = resultLUIS['topScoringIntent']['intent']
        topScoringIntentScore = resultLUIS['topScoringIntent']['score']
        if topScoringIntentScore < 0.9:
            topScoringIntent = 'None'
        #topScoringIntentScore = resultLUIS['topScoringIntent']['score']
        return topScoringIntent
    
    
