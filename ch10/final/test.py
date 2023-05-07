import library

def test_books():
    newbook = library.Library()
    this_book= newbook.random_book()
    print(this_book)
    newbook.full_text(this_book)

test_books()