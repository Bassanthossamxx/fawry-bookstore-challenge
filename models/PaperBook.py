from models.base_book import BaseBook
from services.shipping_service import ShippingService

class PaperBook(BaseBook):
    def deliver(self, address):
        service = ShippingService()
        service.send(self.title, address)

#------------------------- Test ---------------------
'''
paper = PaperBook("123", "idk", 2020, 150)
paper.add_stock(5)
print("Stock after adding:", paper.quantity)

try:
    paper.reduce_stock(2)
    print("Stock after buying 2 books:", paper.quantity)
    paper.deliver("nasr city , cairo")
except Exception as e:
    print("Error in PaperBook:", e)
'''
