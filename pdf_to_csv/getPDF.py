import PyPDF2


def pdfToList(pdfObj):
    #Take in a pdf object and output a list of all lines pdfObj.numPages
    bigList = []
    for i in range(24, pdfObj.numPages):
        page = pdfObj.getPage(i)
        pageText = page.extractText()
        listPlaceholder = pageText.split('\n')
        bigList += listPlaceholder
    return bigList

def getSpellNamesIndex(list):
    indexedLocations = []
    indexedLocation = 
    for i in range(0, len(list)):
        if 'level' in list[i]:
            if list[i-1] == '-':
                if list[i-2][0].isdigit():
                    if list[i-5] = '':
                        indexedLocation=4
                    else:
                        while()


        elif 'cantrip' in list[i]:
            indexedLocations.append(i-1)
    return indexedLocations

#Collect the PDFobject and set the file reader object
spellPDF = PyPDF2.PdfFileReader(open('../Spells.pdf', 'rb'))
#print(spellPDF.getPage(spellPDF.numPages - 1).extractText())
bigOlContent = pdfToList(spellPDF)
spellNameLocations = getSpellNamesIndex(bigOlContent)

for i in spellNameLocations:
    print(bigOlContent[i])


#print(bigOlContent)
