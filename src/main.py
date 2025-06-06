from src.pages.page import Page
import src.pages.das_filament as das_filament


def main():
    page = Page(
        url=das_filament.URL,
        price_selector=das_filament.SELECTOR,
        get_name=das_filament.GET_NAME,
        get_price=das_filament.GET_PRICE
    )
    prices = page.get_prices()
    print(prices)

if __name__ == "__main__":
    main()