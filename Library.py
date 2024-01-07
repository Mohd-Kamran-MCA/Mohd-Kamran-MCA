class Library:
    def __init__(self):
        self.books = {}
        self.lend_books = {}

    def add_book(self, title, author, published_year):
        book_id = uuid.uuid4()
        self.books[book_id] = {
            'title': title,
            'author': author,
            'published_year': published_year,
            'status': 'available'
        }

    def lend_book(self, book_id):
        if book_id in self.books and self.books[book_id]['status'] == 'available':
            self.books[book_id]['status'] = 'lent'
            self.lend_books[book_id] = datetime.now().strftime('%Y-%m-%d')
        else:
            print("Sorry, the book is not available.")

    def return_book(self, book_id):
        if book_id in self.lend_books:
            self.books[book_id]['status'] = 'available'
            del self.lend_books[book_id]
        else:
            print("Sorry, the book was not lent from this library.")

    def display_books(self):
        print("Available Books:")
        for book_id, book_details in self.books.items():
            if book_details['status'] == 'available':
                print(f"Book ID: {book_id} | Title: {book_details['title']} | Author: {book_details['author']} | Published Year: {book_details['published_year']}")

        print("\nLent Books:")
        for book_id, lend_date in self.lend_books.items():
            print(f"Book ID: {book_id} | Lend Date: {lend_date}")
