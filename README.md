# Library Manager

**Student:** Manisha Sharma  
**GitHub:** [manisha-sharma](https://github.com/manisha-sharma)

Python OOP assignment: abstract `LibraryItem`, child types (`Book`, `Magazine`, `DVD`), and `Member` borrow/return rules. Demonstrates inheritance, polymorphism, encapsulation, and `ValueError` handling.

## Files

- `models.py` — classes
- `main.py` — demo (mixed-item late fees, borrow/return errors, private `__available`)
- `README.md` — this file

## Run

```bash
python3 main.py
```

## Deliverables

### 1. Why is `LibraryItem` abstract? What happens if you instantiate it?

`LibraryItem` is a shared template, not a real catalog item. Every item must have its own late-fee rule (`Book` Rs 2/day, `Magazine` Rs 1/day, `DVD` Rs 5/day). Marking `late_fee` with `@abstractmethod` forces each child to implement that rule.

Calling `LibraryItem("x", 1)` raises:

`TypeError: Can't instantiate abstract class LibraryItem without an implementation for abstract method 'late_fee'`

That is intentional: you can only construct concrete types like `Book`.

### 2. How does the mixed-list loop show polymorphism?

`main.py` builds one list of different types:

```python
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
```

There is no `if isinstance(...)` and no check of the type name. Each object still runs **its own** `late_fee`: Book → Rs 6, Magazine → Rs 3, DVD → Rs 15. Same message (`late_fee(3)`), different implementations. That is polymorphism.

### 3. Why is `__available` private? What happens if you read it from outside?

Availability is an internal flag. Outside code should not set it directly, or borrow/return rules can be skipped. The double-underscore name is mangled to `_LibraryItem__available`, so `item.__available` from `main.py` raises `AttributeError`.

The supported way to read it is `item.is_available()`. Borrowing and returning go through `Member.borrow` / `return_item`, which call `mark_borrowed` / `mark_returned`. `__borrowed` on `Member` is private for the same reason; callers use `borrowed_titles()`.
