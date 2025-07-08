from models.DemoBook import DemoBook
from models.PaperBook import PaperBook
class InventoryManager:
    def __init__(self):
        # Dict to hold books
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            #increase stock if already exists
            self.books[book.isbn].add_stock(book.quantity)
        else:
            self.books[book.isbn] = book

    def remove_outdated_books(self, max_age, current_year):
        outdated = []
        for isbn, book in list(self.books.items()):
            if book.is_outdated(current_year, max_age):
                outdated.append(book)
                del self.books[isbn]
        return outdated

    def buy_book(self, isbn, quantity, email=None, address=None):
        if isbn not in self.books:
            raise ValueError("Warning! : Book not found in inventory")

        book = self.books[isbn]

        #For demo books
        if not book.is_sellable():
            raise ValueError("Warning! : This book is not for sale")

        # Stock check and reduce
        book.reduce_stock(quantity)

        # Deliver to either email or address based on book type
        book.deliver(email or address)

        # Return total price
        return book.price * quantity
