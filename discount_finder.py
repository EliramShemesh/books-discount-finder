# discount_finder.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Optional: If you prefer to automatically manage ChromeDriver, uncomment:
# from webdriver_manager.chrome import ChromeDriverManager

class Book:
    """A simple class to represent a book."""
    def __init__(self, title: str, price: float, rating: int):
        self.title = title
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"{self.title} - £{self.price:.2f} - {self.rating} star(s)"


class DiscountFinder:
    """
    This class uses Selenium to scrape the Books to Scrape website and
    finds books with prices below a given threshold (simulated discount).
    """
    def __init__(self, base_url: str = "http://books.toscrape.com/", price_threshold: float = 20.0):
        self.base_url = base_url
        self.price_threshold = price_threshold
        # Initialize the Chrome WebDriver.
        # If using webdriver-manager, you can do:
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.discounted_books = []

    def start(self):
        """Starts the browser and navigates to the homepage."""
        self.driver.get(self.base_url)
        time.sleep(2)  # Allow time for the page to load
        self.find_discounts()

    def find_discounts(self):
        """
        Iterates over all pages on the site and processes each page to look for discounted books.
        """
        while True:
            self.parse_page()
            # Check if a "next" button exists to go to the next page.
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, "li.next > a")
                next_button.click()
                time.sleep(2)  # Wait for the next page to load
            except Exception:
                # No next button found—end of pagination.
                break

    def parse_page(self):
        """
        Parses the current page for books, extracts title, price, and rating.
        Books below the price threshold are added to the list.
        """
        # Each book is contained in an <article class="product_pod">
        books = self.driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        for book_elem in books:
            try:
                # Extract the title from the <a> tag in the <h3> element.
                title_elem = book_elem.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
                title = title_elem.get_attribute("title")

                # Extract the price from the <p> element with class "price_color".
                price_text = book_elem.find_element(By.CSS_SELECTOR, "p.price_color").text
                # Remove the currency symbol (assumes the symbol is at the start) and convert to float.
                price = float(price_text.lstrip("£"))

                # Extract the rating from the class of the <p> element.
                rating_elem = book_elem.find_element(By.CSS_SELECTOR, "p.star-rating")
                rating = self.convert_rating(rating_elem.get_attribute("class"))

                # If the price is below the threshold, consider it “discounted”
                if price < self.price_threshold:
                    self.discounted_books.append(Book(title, price, rating))
            except Exception as e:
                print(f"Error processing a book element: {e}")

    def convert_rating(self, class_string: str) -> int:
        """
        Converts the rating from the class attribute string to an integer.
        For example, if the class string is "star-rating Three", this returns 3.
        """
        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        classes = class_string.split()
        # Look for a rating word in the classes
        for cls in classes:
            if cls in rating_map:
                return rating_map[cls]
        return 0  # Default if not found

    def print_results(self):
        """Sorts and prints the discounted books found."""
        # Sort books by price (lowest first)
        self.discounted_books.sort(key=lambda book: book.price)
        print("\nDiscounted Books (price below £{:.2f}):".format(self.price_threshold))
        for book in self.discounted_books:
            print(book)

    def close(self):
        """Closes the browser."""
        self.driver.quit()


if __name__ == "__main__":
    # Set the discount threshold here (e.g., £20.00)
    finder = DiscountFinder(price_threshold=20.0)
    try:
        finder.start()
        finder.print_results()
    finally:
        finder.close()
