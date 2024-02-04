from pypdf import PdfWriter, PdfReader
from constants import *

pdf_loaded = PdfReader(open(DEFAULT_PDF_FILEPATH, "rb"))
out = PdfWriter()

print(pdf_loaded._get_page(0))
