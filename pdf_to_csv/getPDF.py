import PyPDF2
from getPDF_functions import *
from classes.spell import *

def spellFormat(array):
    pass


#Collect the PDFobject and set the file reader object
spellPDF = PyPDF2.PdfFileReader(open('../Spells.pdf', 'rb'))
#print(spellPDF.getPage(spellPDF.numPages - 1).extractText())
bigOlContent = pdfToList(spellPDF, 26)
spellNameLocations = getSpellNamesIndex(bigOlContent)
spellArray = arrayTheArray(bigOlContent, spellNameLocations)
print(spellArray[-1])
#Print all da names
#for i in range(1, len(spellNameLocations)):
    #print(bigOlContent[spellNameLocations[i-1]:spellNameLocations[i]-1])
#print(bigOlContent)
