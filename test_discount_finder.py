import pytest
from discount_finder import DiscountFinder, Book

# Unit Tests

def test_convert_rating():
    finder = DiscountFinder()
    # Test with each rating word
    assert finder.convert_rating("star-rating One") == 1
    assert finder.convert_rating("star-rating Two") == 2
    assert finder.convert_rating("star-rating Three") == 3
    assert finder.convert_rating("star-rating Four") == 4
    assert finder.convert_rating("star-rating Five") == 5

    # Test with additional CSS classes
    assert finder.convert_rating("star-rating Three extra-class") == 3

    # Test with no valid rating word
    assert finder.convert_rating("star-rating") == 0

def test_book_repr():
    book = Book("Test Book", 19.99, 4)
    expected = "Test Book - £19.99 - 4 star(s)"
    assert repr(book) == expected

# Integration Test

@pytest.mark.integration
def test_discount_finder_integration():
    """
    Integration test for DiscountFinder.
    It opens a browser, scrapes the Books to Scrape website with a high threshold
    (so most books are considered 'discounted'), and ensures that some discounted
    books are found.
    """
    finder = DiscountFinder(price_threshold=50.0)
    try:
        finder.start()
        assert len(finder.discounted_books) > 0
    finally:
        finder.close()
