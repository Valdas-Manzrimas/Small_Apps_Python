import PyPDF2

fileobject = open('abc.pdf', 'rb')

pdfFileReader = PyPDF2.PdfReader(fileobject)

exctractedText = ""

for pageNum in range((len(pdfFileReader.pages))):
    pdfPageObj = pdfFileReader.pages[pageNum]

    exctractedText += pdfPageObj.extract_text()

fileobject.close()

print(exctractedText)