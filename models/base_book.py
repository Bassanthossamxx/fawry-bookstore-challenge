class BaseBook:
    def __init__(self, isbn, title, year, price):
        self.isbn = isbn
        self.title = title
        self.year = year
        self.price = price
        self.quantity = 0
    def add_stock(self, quantity):
        if quantity <0:
            raise ValueError("Warning! : Can't add negative stock")
        self.quantity += quantity
    def reduce_stock(self, quantity):
        if quantity>self.quantity:
            raise ValueError("Warning! : No enough stock available")
        self.quantity -= quantity
    def is_outdated(self,max_age,current_year):
        return (current_year - self.year) > max_age #it return true or false value
    def is_sellable(self):
        return True  # Default: sellable


#------------------------- Test ---------------------
'''
book = BaseBook("123", "idk", 2020, 150)
print(book.price)
book.add_stock(10)
print(book.quantity)  # 10

book.reduce_stock(2)
print(book.quantity)  # 8

print(book.is_outdated(10,2025)) #false
'''

