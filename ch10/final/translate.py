import requests
import library
class Translate:
    def __init__(self, language = "en")
        """
        initialize a translator
        args: desired_language is a string that will determine which language this translator converts to
        """
        self.url = "https://libretranslate.com"
        self.language = language

    def get(self, text):
        """
        gets the language of a text
        args: text to detect
        """
        add_on = "/detect"
        response = requests.get(self.url+add_on, q = text)
        language_detected = response.jsor()
        return language_detected
    
    def list_of_languages(self):
        """
        get the list of languages the API can handle
        """
        add_on = "/languages"
        response = requests.get(self.url+add_on)
        language_list = response.jsor()
        print("Available languages include:")
        for language in language_list:
            print(language["name"])
        return language_list
    
    def set_language(self, language_list):
        """
        sets the language to translate to
        args: list of possible languages
        """
        new_language = input("What language would you like to translate to?")
        for language in language_list:
            if language["name"] == new_language:
                self.language = language["code"]
            else:
                print("That is not an accepted language")
    


    def translate(self, text):
        """
        translates a text from one language to another
        args: text to translate
        """


