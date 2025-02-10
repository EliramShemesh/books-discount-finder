# Discount Finder

Discount Finder is a Python project that uses Selenium to scrape the [Books to Scrape](http://books.toscrape.com/) website to find "discounted" books based on a price threshold. This project is built using object‑oriented programming (OOP) principles and includes tests written with [pytest](https://docs.pytest.org/).

## Features

- **Web Scraping with Selenium:** Automates browser actions to scrape book data.
- **Discount Detection:** Filters books priced below a specified threshold.
- **OOP Design:** Implements a clear, modular design with classes.
- **Testing:** Includes both unit tests and an integration test using pytest.

## Requirements

- Python 3.6+
- [Selenium](https://www.selenium.dev/)
- A compatible browser driver (e.g., [ChromeDriver](https://chromedriver.chromium.org/) for Chrome)
- [pytest](https://docs.pytest.org/)
- *(Optional)* [webdriver-manager](https://pypi.org/project/webdriver-manager/) for automatic driver management

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discount-finder.git
   cd discount-finder
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

You can install the required packages using pip:

bash
Copy
Edit
pip install selenium pytest
If you prefer using webdriver-manager for easier driver handling:

bash
Copy
Edit
pip install webdriver-manager
Alternatively, you can create a requirements.txt file with:

txt
Copy
Edit
selenium
pytest
# webdriver-manager  # Uncomment if you choose to use it
And then install with:

bash
Copy
Edit
pip install -r requirements.txt
Usage
To run the discount finder application:

Run the application:

bash
Copy
Edit
python discount_finder.py
This script will:

Launch a Chrome browser.
Navigate to Books to Scrape.
Scrape the site for books with prices below the default threshold (£20.00).
Print the list of discounted books to the console.
Modify the Discount Threshold:

You can change the discount threshold by editing the instantiation of the DiscountFinder class in the main block of discount_finder.py:

python
Copy
Edit
if __name__ == "__main__":
    finder = DiscountFinder(price_threshold=20.0)  # Change the threshold as needed.
Testing
This project uses pytest for testing. The tests are divided into:

Unit Tests: Test internal methods (e.g., rating conversion, Book representation).
Integration Test: An end‑to‑end test that uses Selenium to scrape the live site.
Running Tests
Run all tests (unit tests by default):

bash
Copy
Edit
pytest --maxfail=1 --disable-warnings -q
Run the integration test:

Integration tests are marked with @pytest.mark.integration. To run them, execute:

bash
Copy
Edit
pytest -q --maxfail=1 -m integration
Note: Integration tests require a live browser session. Ensure you have the appropriate WebDriver and a display (or use headless mode) configured.

Project Structure
bash
Copy
Edit
.
├── discount_finder.py        # Main application code
├── test_discount_finder.py   # Pytest test suite
└── README.md                 # This readme file
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

