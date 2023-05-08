import library
import dictionary
import reading_list
def main():
    local_lib = library.Library()
    your_list = reading_list.Reading_list()
    your_list.view_list()
    newbooks = int(input("How many new books would you like to view?"))
    for i in range(0, newbooks):
        newbook = local_lib.random_book()
        print(newbook["title"])
        def_loop = True
        while def_loop:
            if input("Would you like to look up the meaning of a word in the title of this book") == "yes":
                word = input("Which word?")
                word_dict = dictionary.Dictionary(word)
                word_dict.get()
            else:
                def_loop = False
        print("")
        your_list.add_to_list(newbook)
        print("")
    link_loop = True
    while link_loop:
        if input("Would you like to get the link for a book on your reading list?") == "yes":
            title = input("What is the title of the book?")
            for book in your_list.reading_list:
                if title == book["title"]:
                    print(local_lib.find_url(book))
        else:
            link_loop = False
    print("")
    remove_loop = True
    while remove_loop:
        if input("Would you like to remove a book from your reading list?") == "yes":
            title = input("What is the title of the book?")
            for book in your_list.reading_list:
                if title == book["title"]:
                    your_list.already_read(book)
                    your_list.view_list()
        else:
            remove_loop = False
    print("")
    your_list.save()
    
main()