import requests
from urllib.request import urlopen
import random
import json
class Library:
    def __init__(self):
        """
        initiate the book class
        """
        self.url = "https://gutendex.com/books"
        self.reading_list = []

    def get(self):
        """
        Get the entire list of books on the Project Gutenberg website
        """
        response = requests.get(self.url)
        main_dict = response.json()
        list_of_books = main_dict["results"]
        return list_of_books
    
    def load_reading_list(self):
        """
        Copy a saved reading list into self.reading_list
        """
        file_name = input("What is the name of your reading list?")
        self.reading_list = json.load(open(file_name))
    
    def random_book(self):
        """
        Get a dictionary describing a random book available on the Project Gutenberg website
        """
        list_of_books = self.get()
        num_books = len(list_of_books)
        place_in_list = random.randint(0,num_books-1)
        your_book = list_of_books[place_in_list]
        return your_book
    
    def view_list(self):
        """
        View the current reading list, titles only
        """
        print("Your reading list currently contains:")
        for item in self.reading_list:
            print(item["title"])

    def add_to_list(self, newbook):
        """
        add a book to the reading list
        args: newbook is a dictionary describing a book on the Project Gutenberg website
        """
        print(newbook["title"])
        if input("Do you want to add this book to your reading list?")== "yes":
            self.reading_list.append(newbook)
        self.view_list()
    
    def book_club(self):
        """
        Offers the user a random book to add to their reading list
        """
        self.add_to_list(self.random_book())
    
    def find_url(self, book_to_find):
        """
        returns the url for a plain text version of the book
        """
        #!!! not all books have a plain text version
        links = book_to_find["formats"]
        url = links["text/plain"]
        return url
    
    def full_text(self, book_to_find):
        """
        returns the full plain text of a book
        """
        #!!! has some strange \r and \n marks
        url = self.find_url(book_to_find)
        text = urlopen(url).read()
        return text

    
    def already_read(self, read_book):
        """
        removes a book from the reading list
        """
        self.reading_list.remove(read_book)
        



    