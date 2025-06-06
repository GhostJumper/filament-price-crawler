import re

URL = "dasfilament.de/filament-spulen/pla-1-75-mm/"
SELECTOR = ".product--info"

GET_NAME = lambda text: text.split("\n")[0]
GET_PRICE = lambda text: re.findall(r"\d+,\d+ €", text)[1].split()[0]