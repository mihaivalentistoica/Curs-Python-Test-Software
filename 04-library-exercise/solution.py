import unittest
from .library import Book, Library


class BookInitTestCase(unittest.TestCase):
    def test_init(self):
        b = Book("Hamlet", "William Shakespeare")
        self.assertEqual(b.title, "Hamlet")
        self.assertEqual(b.author, "William Shakespeare")
        self.assertEqual(b.copies, 1)
        self.assertEqual(b.available, 1)

    def test_init_with_parameters(self):
        b = Book("1984", "George Orwell", copies=3, available=2)
        self.assertEqual(b.title, "1984")
        self.assertEqual(b.author, "George Orwell")
        self.assertEqual(b.copies, 3)
        self.assertEqual(b.available, 2)

    def test_availability(self):
        b = Book("Anna Karenina", "Leo Tolstoy", available=0)
        self.assertFalse(b.is_available())
        b.available = 1
        self.assertTrue(b.is_available())

    def test_pretty_name(self):
        title = "The Divine Comedy"
        author = "Dante Alighieri"
        b = Book(title, author)
        self.assertEqual(b.pretty_name(), '"The Divine Comedy" by Dante Alighieri')


class BookBorrowTestCase(unittest.TestCase):
    title = "Don Quixote"
    author = "Miguel de Cervantes Saavedra"

    def test_borrow_positive(self):
        b = Book(self.title, self.author)
        expected = f'You have borrowed "{self.title}" by {self.author}'
        self.assertEqual(b.borrow(), expected)
        self.assertEqual(b.available, 0)
        self.assertEqual(b.copies, 1)

    def test_borrow_multiple_copies_positive(self):
        b = Book(self.title, self.author, copies=10, available=2)
        expected = f'You have borrowed "{self.title}" by {self.author}'
        self.assertEqual(b.borrow(), expected)

        self.assertEqual(b.available, 1)
        self.assertEqual(b.borrow(), expected)
        self.assertEqual(b.available, 0)
        self.assertEqual(b.copies, 10)

    def test_borrow_negative(self):
        b = Book(self.title, self.author, copies=999, available=0)
        self.assertEqual(b.borrow(), "You are unable to borrow this book, sorry!")
        self.assertEqual(b.available, 0)
        self.assertEqual(b.copies, 999)


class BookReturnTestCase(unittest.TestCase):
    title = "The Illiad"
    author = "Homer"

    def test_return_positive(self):
        b = Book(self.title, self.author, available=0)
        self.assertEqual(b.return_book(), "Thank you!")
        self.assertEqual(b.available, 1)
        self.assertEqual(b.copies, 1)

    def test_return_multiple_copies_positive(self):
        b = Book(self.title, self.author, copies=10, available=8)
        self.assertEqual(b.return_book(), "Thank you!")
        self.assertEqual(b.available, 9)
        self.assertEqual(b.return_book(), "Thank you!")
        self.assertEqual(b.available, 10)
        self.assertEqual(b.copies, 10)

    def test_return_negative(self):
        b = Book(self.title, self.author, copies=999, available=999)
        self.assertEqual(
            b.return_book(), "This is impossible! All the copies are already there."
        )
        self.assertEqual(b.available, 999)
        self.assertEqual(b.copies, 999)


class LibraryInventoryTestCase(unittest.TestCase):
    def test_library_init(self):
        l = Library()
        self.assertDictEqual(l.books_by_title, {})

    def test_add_new_book(self):
        l = Library()
        b = Book("War and Peace", "Leo Tolstoy")
        l.add_book(b)
        self.assertEqual(l.books_by_title, {b.title: b})

    def test_add_existing_book(self):
        l = Library()
        b = Book("War and Peace", "Leo Tolstoy")
        l.add_book(b)
        l.add_book(b)
        self.assertEqual(l.books_by_title, {b.title: b})

    def test_remove_existing_book(self):
        l = Library()
        b = Book("War and Peace", "Leo Tolstoy")
        l.add_book(b)
        l.remove_book(b)
        self.assertDictEqual(l.books_by_title, {})

    def test_remove_nonexistent_book(self):
        l = Library()
        b = Book("War and Peace", "Leo Tolstoy")
        l.remove_book(b)
        self.assertDictEqual(l.books_by_title, {})

    def test_status_negative(self):
        l = Library()
        self.assertFalse(l.check_book_status("War and Peace"))

    def test_status_positive(self):
        l = Library()
        b = Book("War and Peace", "Leo Tolstoy")
        l.add_book(b)
        self.assertTrue(l.check_book_status("War and Peace"))


class LibraryBorrowTestCase(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("The Tin Drum", "Gunter Grass")
        self.library.add_book(self.book)

    def test_borrow_nonexistent(self):
        result = self.library.borrow("XYZ")
        self.assertEqual(result, "We do not have XYZ. Try something else.")
        self.assertEqual(self.library.books_by_title[self.book.title].copies, 1)
        self.assertEqual(self.library.books_by_title[self.book.title].available, 1)

    def test_borrow_book(self):
        self.book.available = 1
        self.book.copies = 1
        result = self.library.borrow(self.book.title)
        self.assertEqual(result, 'You have borrowed "The Tin Drum" by Gunter Grass')
        self.assertEqual(self.library.books_by_title[self.book.title].copies, 1)
        self.assertEqual(self.library.books_by_title[self.book.title].available, 0)

    def test_borrow_book_with_multiple_copies(self):
        self.book.available = 2
        self.book.copies = 4
        result = self.library.borrow(self.book.title)
        self.assertEqual(result, 'You have borrowed "The Tin Drum" by Gunter Grass')
        self.assertEqual(self.library.books_by_title[self.book.title].copies, 4)
        self.assertEqual(self.library.books_by_title[self.book.title].available, 1)


class LibraryReturnTestCase(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("The Tin Drum", "Gunter Grass")
        self.library.add_book(self.book)

    def test_return_book(self):
        self.book.available = 0
        self.book.copies = 1
        result = self.library.return_book(self.book.title)
        self.assertEqual(result, "Thank you!")
        self.assertEqual(self.library.books_by_title[self.book.title].copies, 1)
        self.assertEqual(self.library.books_by_title[self.book.title].available, 1)

    def test_return_book_with_multiple_copies(self):
        self.book.available = 98
        self.book.copies = 100
        result = self.library.return_book(self.book.title)
        self.assertEqual(result, "Thank you!")
        result = self.library.return_book(self.book.title)
        self.assertEqual(result, "Thank you!")
        self.assertEqual(self.library.books_by_title[self.book.title].copies, 100)
        self.assertEqual(self.library.books_by_title[self.book.title].available, 100)

    def test_impossible_return(self):
        self.book.available = 1
        self.book.copies = 1
        result = self.library.return_book(self.book.title)
        self.assertEqual(
            result, "This is impossible! All the copies are already there."
        )
        self.assertEqual(self.library.books_by_title[self.book.title].copies, 1)
        self.assertEqual(self.library.books_by_title[self.book.title].available, 1)


bookSuite = unittest.TestSuite(
    [
        BookInitTestCase("test_init"),
        BookInitTestCase("test_init_with_parameters"),
        BookInitTestCase("test_availability"),
        BookInitTestCase("test_pretty_name"),
        BookBorrowTestCase("test_borrow_positive"),
        BookBorrowTestCase("test_borrow_multiple_copies_positive"),
        BookBorrowTestCase("test_borrow_negative"),
        BookReturnTestCase("test_return_positive"),
        BookReturnTestCase("test_return_multiple_copies_positive"),
        BookReturnTestCase("test_return_negative"),
    ]
)

librarySuite = unittest.TestSuite(
    [
        LibraryInventoryTestCase("test_library_init"),
        LibraryInventoryTestCase("test_add_new_book"),
        LibraryInventoryTestCase("test_add_existing_book"),
        LibraryInventoryTestCase("test_remove_existing_book"),
        LibraryInventoryTestCase("test_remove_nonexistent_book"),
        LibraryInventoryTestCase("test_status_negative"),
        LibraryInventoryTestCase("test_status_positive"),
        LibraryBorrowTestCase("test_borrow_nonexistent"),
        LibraryBorrowTestCase("test_borrow_book"),
        LibraryBorrowTestCase("test_borrow_book_with_multiple_copies"),
        LibraryReturnTestCase("test_return_book"),
        LibraryReturnTestCase("test_return_book_with_multiple_copies"),
        LibraryReturnTestCase("test_impossible_return"),
    ]
)
