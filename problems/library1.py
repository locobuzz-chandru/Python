class Book:
    def __init__(self, book_id, title, author, genre, borrowed=False, borrower=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = borrowed
        self.borrower = borrower


class Library:
    def __init__(self, book=None):
        self.book = book
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, book):
        new_node = Library(book)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if temp.book.book_id > book.book_id:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
            if temp.next.book.book_id > book.book_id:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        res = []
        while temp:
            res.append(temp.book)
            temp = temp.next
        return res

    def get_total_books(self):
        return len(self.display())

    def get_available_books(self):
        return len([book.book_id for book in self.display() if not book.borrowed])

    def get_borrowed_books(self):
        return len([book.book_id for book in self.display() if book.borrowed])

    def get_books_by_author(self, author):
        return [book.title for book in self.display() if book.author == author]

    def get_books_by_genre(self, genre):
        return [book.title for book in self.display() if book.genre == genre]

    def _get_book_by_id(self, book_id):
        book = list(filter(lambda book: book.book_id == book_id, self.display()))
        if book:
            return book[0]
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


if __name__ == "__main__":
    L = LinkedList()
    L.display()
    go = Book(book_id=5, title='Go', author='C', genre='Programming')
    python = Book(book_id=1, title='Python', author='A', genre='Programming')
    php = Book(book_id=6, title='PHP', author='C', genre='Programming')
    c = Book(book_id=2, title='C', author='B', genre='Programming')
    typescript = Book(book_id=4, title='Typescript', author='B', genre='Programming')
    java = Book(book_id=3, title='JAVA', author='A', genre='Programming')

    for b in [python, c, java, typescript, go, php]:
        L.add_book(b)
    # print(L.display())
    # print(L.get_total_books())
    # print(L.get_available_books())
    # print(L.get_borrowed_books())
    # print(L.get_books_by_author('B'))
    # print(L.get_books_by_genre('Programming'))
    # print(L.borrow_book(1, 'chandru'))
    # print(L.return_book(1))
    # print(L.get_available_books())
    # print(L.get_borrowed_books())
    print(L.get_book_details(1))