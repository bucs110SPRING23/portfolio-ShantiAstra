import json
class Reading_list:
    def __init__(self, name = "your_reading_list"):
        """
        Load a saved reading list if one exists. If not, make an empty list
        """
        if input("Do you have a reading list saved") == "yes":
            file_name = str(input("What is the name of the file?")) + ".json"
            openfile = open(file_name)
            self.reading_list = json.load(openfile)
            openfile.close()
        else:
            self.reading_list = []
        print("")
        self.name = name
    
    def view_list(self):
        """
        View the current reading list, titles only
        """
        print("Your reading list currently contains:")
        for item in self.reading_list:
            print(item["title"])
        print("")
    
    def add_to_list(self, newbook):
        """
        add a book to the reading list
        args: newbook is a dictionary describing a book on the Project Gutenberg website
        """
        if input("Do you want to add this book to your reading list?")== "yes":
            self.reading_list.append(newbook)
        self.view_list()
    
    def already_read(self, read_book):
        """
        removes a book from the reading list
        args: the dictionary describing the book to be removed
        """
        self.reading_list.remove(read_book)
    
    def save(self):
        """
        saves the reading list to a file
        """
        newfile = open(self.name + ".json", "w")
        json_list = json.dumps(self.reading_list)
        newfile.write(json_list)
        newfile.close()
        self.view_list()
        print(f"Your reading list has been saved for later use with the file name {self.name}")
