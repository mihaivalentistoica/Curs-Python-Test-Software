class Book:
    def __init__(self, title, author, copies=1, available=1):
        if type(title) != str or type(author) != str or type(copies) != int or type(available) != int:
            raise TypeError

        if available > copies or available < 0 or copies <= 0:
            raise ValueError

        self.title = title
        self.author = author
        self.copies = copies
        self.available = available

    def is_available(self):
        return self.available > 0

    def borrow(self):
        if self.is_available():
            self.available -= 1
            return f"You have borrowed {self.pretty_name()}"
        else:
            return "You are unable to borrow this book, sorry!"

    def return_book(self):
        if self.available < self.copies:
            self.available += 1
            return "Thank you!"
        else:
            return "This is impossible! All the copies are already there."

    def pretty_name(self):
        return f'"{self.title}" by {self.author}'


class Library:
    def __init__(self):
        self.books_by_title = {}

    def add_book(self, book):
        if book.title not in self.books_by_title:
            self.books_by_title[book.title] = book

    def remove_book(self, book):
        if book.title not in self.books_by_title:
            return
        del self.books_by_title[book.title]

    def check_book_status(self, title):
        return (
            title in self.books_by_title and self.books_by_title[title].is_available()
        )

    def borrow(self, title):
        if title not in self.books_by_title:
            return f"We do not have {title}. Try something else."
        return self.books_by_title[title].borrow()

    def return_book(self, title):
        if title not in self.books_by_title:
            return f"We do not have {title}. Try something else."
        return self.books_by_title[title].return_book()
