from helium import start_chrome, find_all, kill_browser, Text, S

def get_prices(url: str, price_selector: str) -> str:
    browser = start_chrome(url, headless=True)
    try:
        price_elements = find_all(S(price_selector))
        if price_elements:
            for element in price_elements:
                text = element.web_element.text
                text_parts = text.split("\n")
                print(text)
        else:
            return "No prices not found"
    finally:
        kill_browser()

def main():
    url = "dasfilament.de/filament-spulen/pla-1-75-mm/"
    price_selector = ".product--info"  # Change this to the actual CSS selector for the price
    get_prices(url, price_selector)

if __name__ == "__main__":
    main()