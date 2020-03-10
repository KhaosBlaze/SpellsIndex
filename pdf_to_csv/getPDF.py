import PyPDF2
from getPDF_functions import *
from classes.spell import *


#Testing Variables
endingPage = 30
spellNumber = 5

#Collect the PDFobject and set the file reader object
spellPDF = PyPDF2.PdfFileReader(open('../Spells.pdf', 'rb'))
#print(spellPDF.getPage(spellPDF.numPages - 1).extractText())
bigOlContent = pdfToList(spellPDF, endingPage)
#Get index of where each spell starts
spellNameLocations = getSpellNamesIndex(bigOlContent)
spellArray = arrayTheArray(bigOlContent, spellNameLocations)

spellFormated = []
for spell in spellArray:
    spellFormated.append(spellFormat(spell))

#print(spellArray[spellNumber])
#test = spellFormat(spellArray[spellNumber])
#print(test)

for a in spellFormated:
    print(a)
