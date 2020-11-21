#To read PDF file using Python pip install pypdf2
#To Read text (Text to speech) pip install pyaudio, pip install pyttsx3
#https://pypi.org/project/pyttsx3/

import pyttsx3
import PyPDF2

speaker = pyttsx3.init()

book = open("t2a111.pdf", "rb")
pdfr = PyPDF2.PdfFileReader(book)

pages = pdfr.numPages
print("Number of Pages in the PDF are: " + str(pages))

fromPageNo = int(input("Enter the Page from where you want to read: "))

"""VOICE RATE"""
rate = speaker.getProperty('rate')  # getting details of current speaking rate
print(rate)
# speaker.setProperty('rate', 125)    # setting up new voice rate

"""VOLUME"""
volume = speaker.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)
speaker.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = speaker.getProperty('voices')  # getting details of current voice
selvoice = input("Select Voice [0 for male /1 for female]: ")
if (selvoice == 0):
    speaker.setProperty('voice', voices[0].id)
else:
    speaker.setProperty('voice', voices[1].id)


# page+1 #reading pg 10
for num in range(fromPageNo, pages):
    page = pdfr.getPage(fromPageNo)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
