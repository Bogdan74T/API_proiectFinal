from requests_books.books import *

class TestBooks:

    def test_status_code(self):
        response = get_books()
        assert response.status_code == 200, "Status code should be 200"

    def test_get_books_invalid_type(self):
        response = get_books(book_type = 'adventure')
        assert response.status_code == 400, "Status code should be 400"
        assert response.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction." \
            f"Error message is not the expected one." \
            f"Expected: invalid value for querry parameter 'type'." \
            f"Must be one of: fiction, non-fiction., Actual: {response.json()['error']}"


    def test_get_all_books(self):
        response = get_books()
        assert len(response.json()) == 6, "Total number of books should be 6"
        for book in response.json():
            assert 'book' in book.keys()
            assert 'available' in book.keys()
            assert 'name' in book.keys()
            assert 'type' in book.keys()

    def test_get_all_books_limit(self):
        response = get_books(limit=4)
        assert len(response.jason()) == 4, "Total number of books should be 3"
        i=1
        for book in response.json():
            assert book['id'] == i
            i += 1

    def test_get_all_books_type_fiction(self):
        response = get_books(book_type='fiction')
        for book in response.json():
            assert book['type'] == 'fiction','Book type should be fiction'

    def test_get_all_books_type_and_limit(self):
        response = get_books(book_type='fiction', limit=2)
        assert len(response.jason()) == 2, "Number of books returned should be 2"
        for book in response.json():
            assert book['type'] == 'fiction', 'Book type should be fiction'

    def test_get_book(self):
        response = get_book(4)
        assert response.status_code == 200, "Status code should be 200"
        assert response.json()['id']==4, "Id should be 4"

    def test_get_book_wrong_id(self):
        response = get_book(459)
        assert response.status_code == 404, "Status code should be 404"
        assert 'error' in response.json().keys(),""
        assert response.json()['error'] == "No book with id 459", "Error message incorrect"