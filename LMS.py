class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"
    def update_availability(self, status):
        self.available = status
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id}) - Borrowed books: {[book.title for book in self.borrowed_books]}"
    def borrow_book(self, book):
        if book.available:
            book.update_availability(False)
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.update_availability(True)
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        self.books.append(book)
        print("Book",title, "added to the library.")
    def add_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        user = User(user_id, name)
        self.users.append(user)
        print("User", name,  "added to the library.")
    def borrow_book(self):
        user_id = input("Enter user ID: ")
        book_title = input("Enter book title to borrow: ")
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.title.lower() == book_title.lower()), None)
        if user and book:
            user.borrow_book(book)
        else:
            print("User or book not found.")
    def return_book(self):
        user_id = input("Enter user ID: ")
        book_title = input("Enter book title to return: ")
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.title.lower() == book_title.lower()), None)

        if user and book:
            user.return_book(book)
        else:
            print("User or book not found.")

    def search_book(self):
        query = input("Enter book title or author to search: ")
        found_books = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found.")

    def show_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def show_users(self):
        if self.users:
            for user in self.users:
                print(user)
        else:
            print("No users registered.")
def main():
    library = Library()
    while True:
        print("\n📚 Library Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Show All Books")
        print("7. Show All Users")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.add_user()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.search_book()
        elif choice == "6":
            library.show_books()
        elif choice == "7":
            library.show_users()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Wrong choice. Please try again.")
if __name__ == "__main__":
    main()
