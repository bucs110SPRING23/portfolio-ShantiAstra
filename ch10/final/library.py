import requests
import random
import json
class Library:
    def __init__(self):
        """
        initiate the library class
        """
        self.url = "https://gutendex.com/books"

    def __str__(self):
        """
        returns a string describing the library
        """
        return f'This is a api proxy class that gets data from {self.url}'
    
    def get(self):
        """
        Get the entire list of books on the Project Gutenberg website
        """
        response = requests.get(self.url)
        main_dict = response.json()
        list_of_books = main_dict["results"]
        return list_of_books
    
    def random_book(self):
        """
        Get a dictionary describing a random book available on the Project Gutenberg website
        return: the dictionary describing the book
        """
        list_of_books = self.get()
        num_books = len(list_of_books)
        place_in_list = random.randint(0,num_books-1)
        your_book = list_of_books[place_in_list]
        return your_book

    
    def find_url(self, book_to_find):
        """
        returns the url for a plain text version of the book, if it has one
        args: the dictionary that describes the book to be found
        return: the url, if one exists
        """
        links = book_to_find["formats"]
        url = links.get("text/plain")
        if url == None:
            print("This book is not available in the plain text format. Please go to the Project Gutenberg website to find another version")
        else:
            return url
    




    