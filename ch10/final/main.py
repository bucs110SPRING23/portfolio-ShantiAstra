import library
import translate
import library_search
import json
def main():
    local_lib = library.Library()
    translator = translate.Translate()
    if input("Do you have a reading list saved") == "yes":
        local_lib.load_reading_list()
    print("")
    newbooks = int(input("How many new books would you like to view?"))
    for i in range(0, newbooks):
        local_lib.book_club()
        print("")
    translate_loop = True
    while translate_loop:
        if input("Do you need to translate any books from your reading list?") == "yes":
            title = input("What is the title of the book?")
            for book in local_lib.reading_list:
                if title == book["title"]:
                    url = local_lib.find_url(book)
                    #book = translator.change_language(url)
                    print(f'{title} has been translated')
        else:
            translate_loop = False
    print("")
    link_loop = True
    while link_loop:
        if input("Would you like to get the link for a book on your reading list?") == "yes":
            title = input("What is the title of the book?")
            for book in local_lib.reading_list:
                if title == book["title"]:
                    print(local_lib.find_url(book))
        else:
            link_loop = False
    print("")
    lib_loop = True
    while lib_loop:
        if input("Would you like to find libraries that own the book on your reading list?") == "yes":
            title = input("What is the title of the book?")
            for book in local_lib.reading_list:
                if title == book["title"]:
                    new_search = library_search.Library_Search(book)
                    new_search.find_libraries()
        else:
            lib_loop = False
    print("")
    remove_loop = True
    while remove_loop:
        if input("Would you like to remove a book from your reading list?") == "yes":
            title = input("What is the title of the book?")
            for book in local_lib.reading_list:
                if title == book["title"]:
                    local_lib.already_read(book)
                    local_lib.view_list()
        else:
            remove_loop = False
    print("")
    newfilename = "your_reading_list"
    newfile = open(newfilename + ".json", "w")
    json_list = json.dumps(local_lib.reading_list)
    newfile.write(json_list)
    # for book in local_lib.reading_list:
	#     newfile.write(str(book)+"\n")
    newfile.close()
    
main()