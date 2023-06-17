from bst import BinaryTree
import random


class Book:
    def __init__(self, book_id, title, author, genre, borrowed=False, borrower=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = borrowed
        self.borrower = borrower

    def __repr__(self):
        return f"{self.id}"

    def __str__(self):
        return self.__repr__()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = BinaryTree()

    def add_book(self, book):
        self.books.add(book)

    def get_total_books(self):
        return self.books.count()

    def _get_books(self):
        return self.books.traverse_inorder()

    def get_available_books(self):
        print(self._get_books())
        return len([book.id for book in self._get_books() if not book.borrowed])

    def get_borrowed_books(self):
        return len([book.id for book in self._get_books() if book.borrowed])

    def get_books_by_author(self, author):
        return [book.title for book in self._get_books() if book.author == author]

    def get_books_by_genre(self, genre):
        return [book.title for book in self._get_books() if book.genre == genre]

    def _get_book_by_id(self, book_id):
        book = self.books.search(book_id)
        if book:
            return book
        raise Exception("book id does not exist")

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
        return f"Book ID : {book.id}\n" \
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
    books = [python, c, java, go, php, typescript]
    random.shuffle(books)
    for b in books:
        library1.add_book(b)
    # print(library1.get_total_books())
    print(books)
    print(library1.get_available_books())
    # print(library1.get_borrowed_books())
    # print(library1.get_books_by_author('A'))
    # print(library1.get_books_by_genre('Programming'))
    # print(library1.borrow_book(1, 'chandru'))
    # print(library1.return_book(1))
    # print(library1.get_book_details(2))
