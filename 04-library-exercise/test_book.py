import unittest
from library import Book

TITLE = 'TITLE'
AUTHOR = 'Author'


class TestBookInit(unittest.TestCase):
    def test_init(self):
        book = Book(title=TITLE, author=AUTHOR, copies=2, available=1)
        self.assertEqual(book.title, TITLE)
        self.assertEqual(book.author, AUTHOR)
        self.assertEqual(book.copies, 2)
        self.assertEqual(book.available, 1)

    def test_init_default_params(self):
        book = Book(title=TITLE, author=AUTHOR)
        self.assertEqual(book.title, TITLE)
        self.assertEqual(book.author, AUTHOR)
        self.assertEqual(book.copies, 1)
        self.assertEqual(book.available, 1)

    def test_init_wrong_type(self):
        with self.assertRaises(TypeError):
            book = Book(title=2, author=32, copies='2', available='3')

    def test_init_wrong_value(self):
        with self.assertRaises(ValueError):
            book = Book(title=TITLE, author=AUTHOR, copies=1, available=2)

    def test_init_negative_value(self):
        with self.assertRaises(ValueError):
            book = Book(title=TITLE, author=AUTHOR, copies=0, available=-2)


class TestBookIsAvailable(unittest.TestCase):
    def test_is_available(self):
        book = Book(title=TITLE, author=AUTHOR, copies=1, available=0)
        self.assertFalse(book.is_available())
        book.available = 1
        self.assertTrue(book.is_available())


class TestBookPrettyName(unittest.TestCase):
    def test_pretty_name(self):
        book = Book(title=TITLE, author=AUTHOR, copies=2, available=2)
        expected = f'"{book.title}" by {book.author}'
        actual = book.pretty_name()
        self.assertEqual(expected, actual)


class TestBookBorrow(unittest.TestCase):
    def test_borrow_available(self):
        available = 2
        book = Book(title=TITLE, author=AUTHOR, copies=2, available=available)
        result = book.borrow()
        self.assertEqual(book.available, available - 1)
        self.assertTrue(book.title in result and book.author in result)

    def test_borrow_unavailable(self):
        available = 0
        book = Book(title=TITLE, author=AUTHOR, copies=2, available=available)
        result = book.borrow()
        self.assertEqual(book.available, available)
        self.assertTrue(type(result) == str)


class TestBookReturnBook(unittest.TestCase):
    def test_return_book_available(self):
        available = 0
        book = Book(title=TITLE, author=AUTHOR, copies=2, available=available)
        result = book.return_book()
        self.assertEqual(book.available, available + 1)
        self.assertEqual(result, "Thank you!")

    def test_return_book_unavailable(self):
        available = 2
        book = Book(title=TITLE, author=AUTHOR, copies=2, available=available)
        result = book.return_book()
        self.assertEqual(book.available, available)
        self.assertEqual(result, "This is impossible! All the copies are already there.")
