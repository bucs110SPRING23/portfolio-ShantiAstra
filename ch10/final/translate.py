import requests
#from requests.auth import HTTPBasicAut
import library
class Translate:
    def __init__(self, language = "en"):
        """
        initialize a translator
        args: desired_language is a string that will determine which language this translator converts to
        """
        self.url = "https://libretranslate.com"
        self.language = language
        self.token = "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"
        

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
        return: the list of languages
        """
        add_on = "/languages"
        response = requests.get(self.url+add_on)
        language_list = response.jsor()
        print("Available languages include:")
        for language in language_list:
            print(language["name"])
        return language_list
    
    def set_language(self):
        """
        sets the language to translate to
        """
        language_list = self.list_of_languages()
        new_language = input("What language would you like to translate to?")
        for language in language_list:
            if language["name"] == new_language:
                self.language = language["code"]
            else:
                print("That is not an accepted language")
    
    def prep_authentication(self):
        """
        generate api for authentication
        return: api key
        """
        # curl --request GET \
        # --url "https://api.github.com/octocat" \
        # --header "Authorization: Bearer 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" \
        # --header "X-GitHub-Api-Version: 2022-11-28"
        pass

    def change_language(self, fileurl):
        """
        translates a text from one language to another
        args: text to translate
        """
        self.set_language()
        add_on = "/translate_file"
        auth = HTTPBasicAuth(apiKey, self.apikey)
        response = requests.get(self.url+add_on, file = fileurl, target = self.language)
        language_list = response.jsor()
        return 


