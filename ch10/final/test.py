import library
import library_search

def test_books():
    newbook = library.Library()
    this_book= newbook.random_book()
    new_search = library_search.Library_Search(this_book)
    new_search.find_libraries()

test_books()