# CTCI 7.5

# who, what, when, where, how, why?
# who is this targeted to? Users
# What main componets does a online book reader have?
# authors can upload and delete books, users can read, turn the page, search page, search for words, search
# for books/authors/genres/categories/ can bookmark book pages, can bookmark books
# The system has the current book being read,
# order of books can be books purchased, read, want to read, want to purchase, most recently read, reading
# What are the main components?
# the e-reader(app), the user, the book store(lot of categories), the users home page(lot of categories),
# in the book store you can view books, add them to your basket, add them to your wishlist, purchase books at checkout,
# you can get books samples. The book store must see if the user is logged in and then upon purhase must need an address for billing and a form of payment.
# another class component is book. Book will have id, information(author, title, co-author, publisher), length(chapters/pages), material, audio-reader,
# another component is the user. The user will hold the books owned, read, sampled, reading, stared, and will allow purchasing power into the book store


class EReader():
    def __init__(self):
        # ? What would be the initiazed state of ereader?
        self.users = {}
        self.library = {}

    def buy(self, book, cost):
        pass

    def star(self, book):
        pass

    def login(self, username, password):
        # set user here
        pass

    def logout(self):
        # make user none
        pass

    def read(self, book):
        # ? would read be its own function or do we turn pages inside the book object? I think we turn pages inside the book object
        # ? because state is being saved on the object. The only access point to changing the book is in the read function
        pass

    def GUI(self):
        pass

    def delete_user(self, user):
        pass

    def create_user(self, info):
        pass


class Page():
    def __init__(self):
        self.text
        self.pages = []


class Book(Page):
    def __init__(self, author, title, length, publisher, genre):
        self.author = author
        self.title = title
        self.length = length
        self.publisher = publisher
        self.genre = genre
        self.bookmarked = []

    def turn_page_forward(self):
        pass

    def turn_page_backward(self):
        pass

    def bookmark_page(self, page_num):
        pass
    #  toggle method on pages

    def highlight(self, page_num):
        pass


class User():
    def __init__(self, name, DOB, location, username, password):
        self.name = name
        self.dob = DOB
        self.location = location
        self.username = username
        self.password = password  # Hash of password and username so data is secure
        self.library = []  # books purchased

    def delete(self):
        """Deletes Account"""
        pass

    def set_account_info(self, name, DOB, location):
        pass

    def get_account_info(self, name, DOB, location):
        pass

    def set_payment_info(self, name, address, card_number, expiration, sec):
        pass

    def get_payment_info(self):
        pass
