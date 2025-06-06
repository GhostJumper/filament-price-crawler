from src.pages.page import Page
from src.pages.page_config import das_filament_config


def main():
    page = Page(
        page_config=das_filament_config
    )
    prices = page.get_prices()
    print(prices)

if __name__ == "__main__":
    main()