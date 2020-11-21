#To read PDF file using Python pip install pypdf2
#To Read text (Text to speech) pip install pyaudio, pip install pyttsx3
#https://pypi.org/project/pyttsx3/

import pyttsx3
import PyPDF2

PDF = Input("Enter the pdf you want to read ?")

book = open("t2a111.pdf",'rb')
pdfr = PyPDF2.PdfFileReader(book)
pages = pdfr.numPages

speaker = pyttsx3.init()

fromPageNo = Input("Enter the Page from where you want to read")
#page+1 #reading pg 10
for num in range(fromPageNo,pages):
    page = pdfr.getPage(9)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
