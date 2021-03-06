from dao.book_repository import BookRepository
from entity.book import Book


class BookController:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def add_book(self, book: Book):
        # TODO validation
        self._book_repo.create(book)

    def get_all_books(self):
        return self._book_repo.find_all()