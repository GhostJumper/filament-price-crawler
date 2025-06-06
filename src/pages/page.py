class Page:
    def __init__(self, url: str, price_selector: str, get_name, get_price):

        self.url = url
        self.price_selector = price_selector
        self.getname = get_name
        self.getprice = get_price

    def get_prices(self) -> list:
        from helium import start_chrome, find_all, kill_browser, S
        import re

        browser = start_chrome(self.url, headless=True)
        prices = []
        try:
            price_elements = find_all(S(self.price_selector))
            if price_elements:
                for element in price_elements:
                    text = element.web_element.text
                    name = self.getname(text)
                    price = self.getprice(text)
                    prices.append({'name': name, 'price': price})
            return prices
        finally:
            kill_browser()
