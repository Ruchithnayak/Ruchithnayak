import re
import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """Fetch the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_emails(content):
    """Extract email addresses using regular expressions."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, content)

def extract_phone_numbers(content):
    """Extract phone numbers using regular expressions."""
    phone_pattern = r'\+?\d{1,3}?[-.\s]??\d{1,4}??[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
    return re.findall(phone_pattern, content)

def extract_prices(content):
    """Extract product prices using regular expressions."""
    price_pattern = r'\$\d+(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(price_pattern, content)

def main():
    # Example URL (replace with your target URL)
    url = "https://example.com"

    print(f"Scraping {url}...\n")
    webpage_content = fetch_webpage(url)
    
    if webpage_content:
        soup = BeautifulSoup(webpage_content, 'html.parser')
        text_content = soup.get_text()  # Extract text content from HTML

        # Extract specific information
        emails = extract_emails(text_content)
        phone_numbers = extract_phone_numbers(text_content)
        prices = extract_prices(text_content)

        # Display results
        print("Emails Found:")
        print(emails if emails else "No emails found.\n")

        print("\nPhone Numbers Found:")
        print(phone_numbers if phone_numbers else "No phone numbers found.\n")

        print("\nPrices Found:")
        print(prices if prices else "No prices found.\n")

if __name__ == "__main__":
    main()
