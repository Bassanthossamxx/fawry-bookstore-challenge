from models.base_book import BaseBook
from services.mail_service import MailService

class EBook(BaseBook):
    def __init__(self, isbn, title, year, price, filetype):
        super().__init__(isbn, title, year, price)
        self.filetype = filetype

    def deliver(self, email):
        service = MailService()
        service.send(self.title, email, self.filetype)

#------------------------- Test ---------------------
"""
ebook = EBook("123", "idk", 2020, 100, "pdf")
ebook.add_stock(3)
print("Stock :", ebook.quantity)

try:
    ebook.reduce_stock(1)
    print("Stock after buying :", ebook.quantity)
    ebook.deliver("bassant@gmail.com")
except Exception as e:
    print("Error in EBook:", e)
"""