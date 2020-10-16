"""
PDF Reader using two text transcription speaker version-3 and PyPDF2
"""
import pyttsx3
import PyPDF2

book = open('book_name.pdf', 'rb')
pdf_Reader = PyPDF2.PdfFileReader(book)
pages = pdf_Reader.numPages  # number of pages
speaker = pyttsx3.init()  # initialize the text transcription
for i in range(12, pages):
    page = pdf_Reader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
