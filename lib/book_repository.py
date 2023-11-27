from lib.book import *

class BookRepository():
        # Initialise with a database connection
        def __init__(self, connection):
            self._connection = connection

        # Retrieve all books
        def all(self):
            # Returns list of Book objects
            rows = self._connection.execute('SELECT * from books')
            books = []
            for row in rows:
                item = Book(row["id"], row["title"], row["author_name"])
                book_string = item.dashed_string()
                books.append(book_string)
            return books

