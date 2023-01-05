from QR_code_scanner import QR_Code_Scanner
from scrapper import Scrapper

s = Scrapper()

c = QR_Code_Scanner(scrapper=s)
c.run()