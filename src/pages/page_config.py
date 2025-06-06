from dataclasses import dataclass
import re

@dataclass
class PageConfig:
    url: str
    selector: str
    get_name: callable
    get_price: callable

das_filament_config = PageConfig(
    url="dasfilament.de/filament-spulen/pla-1-75-mm/",
    selector=".product--info",
    get_name=lambda text: text.split("\n")[0],
    get_price=lambda text: re.findall(r"\d+,\d+ €", text)[1].split()[0],
)
