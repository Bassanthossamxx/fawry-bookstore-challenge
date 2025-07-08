# Bookstore — Fawry N² Dev Slope Challenge #10

A console-based Python bookstore system designed with OOP principles, clean project structure, and extensibility in mind. Built to simulate adding, buying, and managing different types of books like paperbacks, ebooks, and demo copies.

---

## Features

✅ Add books to inventory  
✅ Handle 3 book types:
- **PaperBook** – Shipped physically
- **EBook** – Sent via email
- **DemoBook** – Only for display, not for sale

✅ Buy books using ISBN, quantity, email or address  
✅ Prevent buying unavailable or demo books  
✅ Remove outdated books (by publication year)  
✅ Simulates email and shipping services  
✅ Error handling for missing books or stock issues  
✅ Clean, extensible class-based design

---

## Project Structure

```
fawry-bookstore-challenge/
│
├── main.py                         # Entrypoint with all logic & tests
├── README.md
│
├── inventory/
│   └── manager.py                  # InventoryManager: add, buy, remove
│
├── models/
│   ├── base_book.py               # BaseBook with shared logic
│   ├── DemoBook.py                # ShowcaseBook (not for sale)
│   ├── Ebook.py                   # EBook class
│   ├── PaperBook.py               # PaperBook class
│
└── services/
    ├── mail_service.py            # MailService (prints to console)
    └── shipping_service.py        # ShippingService (prints to console)
```

---

## How to Run

```bash
python main.py
```

You’ll see output in the console that shows all actions and handled errors.

---

## Sample Output

```
Book Store system : 
--------------------------Try buying PaperBook--------------------------
Book Store: Shipping 'paperbook' to address: nasr city
Book Store: Paid 240 EGP for paper book
--------------------------Try buying EBook--------------------------
Book Store: Sending 'Ebook.try' to email: bassant@gmail.com
Book Store: Paid 150 EGP for ebook
--------------------------Try buying demo book (should fail)--------------------------
 Book Store: Expected error buying demo: Warning! : This book is not for sale
--------------------------Try buying unknown ISBN Book --------------------------
Book Store: Error for unknown ISBN: Warning! : Book not found in inventory
 Book Store: Removed outdated book: paperbook (2008)
 Book Store: Removed outdated book: Demo (2020)
```

---

## OOP Concepts Used

* Inheritance: `PaperBook`, `EBook`, `DemoBook` all inherit from `BaseBook`
* Polymorphism: `deliver()` method behaves differently across book types
* Encapsulation: Book attributes are managed internally
* No type-checking: System relies on class behavior, not instance checks
* Extensibility: Easily add new book types without changing manager logic

---

## Notes

* All actions are simulated via `print()` (no actual email/shipping logic)
* Print output is always prefixed with `Book Store:` for consistency
* You can add more book types by creating new files in `models/` and implementing `.deliver()` and `.is_sellable()` as needed

---

bassant hossam 