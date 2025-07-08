from inventory.manager import InventoryManager
from models.PaperBook import PaperBook
from models.Ebook import EBook
from models.DemoBook import DemoBook

print("Book Store system : ")

# init manager
manager = InventoryManager()

# Add books
paper = PaperBook("PB01", "paperbook",  2008, 120)
paper.quantity = 5
manager.add_book(paper)

ebook = EBook("EB01", "Ebook", 2022, 150, "try")
ebook.quantity = 3
manager.add_book(ebook)

demo = DemoBook("DB01", "Demo", 2020)
demo.quantity = 1
manager.add_book(demo)

# Buy paper book

print("--------------------------Try buying PaperBook--------------------------")
try:
    paid = manager.buy_book("PB01", 2, address="nasr city")
    print(f"Book Store: Paid {paid} EGP for paper book")
except Exception as e:
    print("Book Store: Error buying paper book:", e)

# Buy ebook
print("--------------------------Try buying EBook--------------------------")
try:
    paid = manager.buy_book("EB01", 1, email="bassant@gmail.com")
    print(f"Book Store: Paid {paid} EGP for ebook")
except Exception as e:
    print("Book Store: Error buying ebook:", e)
print("--------------------------Try buying demo book (should fail)--------------------------")
# Try buying demo book (should fail)
try:
    manager.buy_book("DB01", 1, email="bassant@gmail.com")
except Exception as e:
    print(" Book Store: Expected error buying demo:", e)

# Try buying unknown ISBN

print("--------------------------Try buying unknown ISBN Book --------------------------")
try:
    manager.buy_book("FAKE01", 1, email="bassant@gmail.com")
except Exception as e:
    print("Book Store: Error for unknown ISBN:", e)

# Remove outdated books (older than 10 years)
outdated = manager.remove_outdated_books(max_age=10, current_year=2025)
for book in outdated:
    print(f" Book Store: Removed outdated book: {book.title} ({book.year})")
