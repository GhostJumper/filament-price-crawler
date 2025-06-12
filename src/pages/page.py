from src.pages.page_config import PageConfig

class Page:
    def __init__(self, page_config: PageConfig):
        self.urls = page_config.urls
        self.selector = page_config.selector
        self.getname = page_config.get_name
        self.getprice = page_config.get_price

    def get_prices(self) -> list:
        from helium import start_chrome, find_all, kill_browser, S
        import re
        prices = []
        for url in self.urls:
            browser = start_chrome(url, headless=True)
            try:
                price_elements = find_all(S(self.selector))
                if price_elements:
                    for element in price_elements:
                        text = element.web_element.text
                        name = self.getname(text)
                        price = self.getprice(text)
                        prices.append({'name': name, 'price': price})
            finally:
                kill_browser()
        return prices
