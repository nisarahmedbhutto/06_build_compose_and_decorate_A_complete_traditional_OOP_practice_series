
class Book:
    total_book = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_book += 1


Book.increment_book_count()
Book.increment_book_count()
print(Book.total_book)