from lib.book_repository import *

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_all_books(db_connection): 
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new ArtistRepository

    books = repository.all() # Get all books

    # Assert on the results
    assert books == [
        "1 - Nineteen Eighty-Four - George Orwell",
        "2 - Mrs Dalloway - Virginia Woolf",
        "3 - Emma - Jane Austen",
        "4 - Dracula - Bram Stoker",
        "5 - The Age of Innocence - Edith Wharton",
    ]
