import requests
import json
class Library_Search:
    def __init__(self, book):
        """
        initializes a library search
        args: book is a dict describing a book to search for
        """
        self.url = "https://cdnjs.com/api/libraries"
        self.book = book

    def find_libraries(self):
        """
        return up to 10 CDNJS libraries that have the desired book in them
        """
        
        params = {
            #"search":str(input("What keyword do you want to use to find a library?")),
            "limit":10
            }
        result = requests.get(self.url, params = params)
        print(result)
        #!!! get library names printed somehow
        #print(results[result].name)
        # for library in result:
        #     print(library["name"])