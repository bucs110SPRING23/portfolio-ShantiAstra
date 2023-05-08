import requests
#from urllib.request import urlopen
import random
import json
class Library:
    def __init__(self):
        """
        initiate the library class
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
        file_name = "your_reading_list.txt"
        openfile = open(file_name)
        self.reading_list = json.load(openfile)
        #self.reading_list = file.split("\n")
        #!!!
        print(self.reading_list)
        openfile.close()
    
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
    
    def full_text(self, book_to_find):
        """
        returns the full plain text of a book
        args: the dictionary describing the book
        return: the full text of the book as a string
        """
        #!!! has some strange \r and \n marks
        url = self.find_url(book_to_find)
        text = urlopen(url).read()
        return text

    
    def already_read(self, read_book):
        """
        removes a book from the reading list
        args: the dictionary describing the book to be removed
        """
        self.reading_list.remove(read_book)
        



    