from lib.book import Book 

"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, "Emma", "Jane Austen")
    assert book.id == 1
    assert book.title == "Emma"
    assert book.author_name == "Jane Austen"

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 =  Book(1, "Emma", "Jane Austen")
    book2 =  Book(1, "Emma", "Jane Austen")
    assert book1 == book2

"""
We can format books to strings nicely using __repr__
"""
def test_book_formats_nicely():
    book =  Book(1, "Emma", "Jane Austen")
    assert str(book) == "Book(1, Emma, Jane Austen)"

"""
We can format books to strings in the way the challenge requires using dashed_string
"""
def test_book_formats_for_challenge():
    book =  Book(1, "Emma", "Jane Austen")
    assert book.dashed_string() == "1 - Emma - Jane Austen"




