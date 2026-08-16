class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

book_title=input().strip()
author_name=input().strip()
book_price=float(input())

book_details=Book(book_title, author_name, book_price)

print(f"BOOK DETAILS")
print(f"Title: {book_details.title}")
print(f"Author: {book_details.author}")
print(f"Price: {book_details.price}")




