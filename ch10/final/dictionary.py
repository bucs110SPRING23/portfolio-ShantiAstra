import requests
import json
class Dictionary:
    def __init__(self, word = "error"):
        """
        initialize a dictionary object
        """
        self.url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+str(word)

    def get(self):
        """
        get the definition of the word
        """
        word_data = requests.get(self.url)
        json_data = word_data.json()
        if type(json_data) != list:
            print("No definitions found, please try another dictionary application")
        else:
            for obj in json_data:
                word = obj.get('meanings')
            for obj in word:
                definitions_list = obj.get("definitions")
            definitions = []
            for obj in definitions_list:
                newdef = None
                newdef = obj.get("definition")
                definitions.append(newdef)
            print("definitions:", definitions)
            print("")


