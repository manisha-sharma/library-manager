from models import Book, Magazine, DVD, Member, LibraryItem

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("National Geographic", 2, 120)
dvd = DVD("Inception", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

print("Total items created:", LibraryItem.total_items)

# Borrow / return wrapped in try / except ValueError
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    print("Alice's titles:", alice.borrowed_titles())
    bob.borrow(book)  # already taken
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    fee = alice.return_item(book, days_late=3)
    print("Alice returned the book. Late fee: Rs", fee)
except ValueError as e:
    print("Could not return:", e)

try:
    bob.return_item(book)  # Bob never borrowed the book
except ValueError as e:
    print("Could not return:", e)

# Encapsulation: private __available vs public is_available()
try:
    print(book.__available)
except AttributeError as e:
    print("Cannot read __available from outside:", e)

print("Availability via is_available():", book.is_available())
