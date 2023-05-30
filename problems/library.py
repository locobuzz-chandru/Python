"""
1.  Library class:

    -   Attributes:

        1. name (string)
        2. books (list of Book objects)

    -   Methods:
        1. add_book(book): Add a new book to the library.
        2. get_total_books(): Return the total number of books in the library.
        3. get_available_books(): Return the number of available books.
        4. get_borrowed_books(): Return the number of borrowed books.
        5. get_books_by_author(author): Return a list of books written by a specific author.
        6. get_books_by_genre(genre): Return a list of books in a specific genre.
        7. borrow_book(book_id, borrower): Borrow a book from the library.
        8. return_book(book_id): Return a borrowed book to the library.
        9. get_book_details(book_id): Return the details of a specific book.

2.  Book class:

    -   Attributes

        1. book_id (integer)
        2. title (string)
        3. author (string)
        4. genre (string)
        5. borrowed (boolean)

    -   Methods:
        -   None

---

#### Your task is to implement these classes and write a program to simulate the library management system. The program should allow the user to perform the following operations:

-   [] Add books to the library.
-   [] Retrieve and display the total number of books.
-   [] Retrieve and display the number of available books.
-   [] Retrieve and display the number of borrowed books.
-   [] Retrieve and display a list of books written by a specific author.
-   [] Retrieve and display a list of books in a specific genre.
-   [] Borrow a book from the library.
-   [] Return a borrowed book to the library.
-   [] Retrieve and display the details of a specific book.

"""


class Book:
    def __init__(self, book_id, title, author, genre, borrowed=False, borrower=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = borrowed
        self.borrower = borrower


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        return f"Book '{book.title}' is added"

    def get_total_books(self):
        return f"Total books in library: {len(self.books)}"

    def get_available_books(self):
        return f"Total available books: {len([book.book_id for book in self.books.values() if not book.borrowed])}"

    def get_borrowed_books(self):
        return f"Total burrowed books: {len([book.book_id for book in self.books.values() if book.borrowed])}"

    def get_books_by_author(self, author):
        return f"Books by Author '{author}': {[book.title for book in self.books.values() if book.author == author]}"

    def get_books_by_genre(self, genre):
        return f"Books by genre '{genre}': {[book.title for book in self.books.values() if book.genre == genre]}"

    def _get_book_by_id(self, book_id):
        try:
            return self.books[book_id]
        except KeyError:
            raise Exception("Book is not found")

    def borrow_book(self, book_id, borrower):
        book = self._get_book_by_id(book_id)
        book.borrowed = True
        book.borrower = borrower
        return True

    def return_book(self, book_id):
        book = self._get_book_by_id(book_id)
        book.borrowed = False
        book.borrower = None
        return True

    def get_book_details(self, book_id):
        book = self._get_book_by_id(book_id)
        return f"Book ID : {book.book_id}\n" \
               f"Title   : {book.title}\n" \
               f"Author  : {book.author}\n" \
               f"Genre   : {book.genre}\n"


if __name__ == '__main__':
    python = Book(book_id=1, title='Python', author='A', genre='Programming')
    c = Book(book_id=2, title='C', author='B', genre='Programming')
    java = Book(book_id=3, title='JAVA', author='A', genre='Programming')
    typescript = Book(book_id=4, title='Typescript', author='B', genre='Programming')
    go = Book(book_id=5, title='Go', author='C', genre='Programming')
    php = Book(book_id=6, title='PHP', author='C', genre='Programming')

    library1 = Library(name='L1')
    for b in [python, c, java, typescript, go, php]:
        library1.add_book(b)
    # print(library1.books)
    # print(library1.get_total_books())
    # print(library1.get_available_books())
    # print(library1.get_borrowed_books())
    # print(library1.get_books_by_author('A'))
    # print(library1.get_books_by_genre('Programming'))
    print(library1.borrow_book(11, 'chandru'))
    print(library1.return_book(1))
    print(library1.get_book_details(6))
