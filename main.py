# importing all the required modules
import PyPDF2


from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

filetypes = (
    ('Text files', '*.PDF'),
    ('All files', '*.*'),
)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(title='Select a file...',
    filetypes=filetypes) # show an "Open" dialog box and return the path to the selected file
print(filename)

# creating a pdf reader object
reader = PyPDF2.PdfReader(filename)

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
t = reader.pages[0].extract_text()
number_of_pages = len(reader.pages)
#print(reader.pages[0].extract_text())


import pyttsx3

engine = pyttsx3.init()

for i in range(number_of_pages):
    print("Page No - " + str(i))
    print(reader.pages[i].extract_text())
    engine.say(reader.pages[i].extract_text())
    engine.runAndWait()
