from models.base_book import BaseBook
class DemoBook(BaseBook):
    def __init__(self, isbn, title, year):
        super().__init__(isbn, title, year, price=0.0)


#----------Test---------
""""
demo = DemoBook("789", "Demo Book", 2015)
print(demo.price) # 0.0
"""
