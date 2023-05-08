import requests
import json
class Dictionary:
    def __init__(self, word = "error"):
        """
        initialize a dictionary object
        """
        self.word = word
        self.url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+str(word)

    def __str__(self):
        """
        returns a string that describes the dictionary instance
        """
        return f'This is a dictionary proxy class to look up the word {self.word} from the api at {self.url}'

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


