import PyPDF2


def pdfToList(pdfObj):
    #Take in a pdf object and output a list of all lines pdfObj.numPages
    bigList = []
    for i in range(24, 26):
        #Store page temporarily and convert to text and split to an array
        page = pdfObj.getPage(i)
        pageText = page.extractText()
        listPlaceholder = pageText.split('\n')
        #Add Array to big array
        bigList += listPlaceholder
    return bigList

def spellVerify(text):
    return 'Casting Time:' in text and 'Range:' in text


def getSpellNamesIndex(list):
    #Set empty array to store locations
    indexedLocations = []
    #For while loop logic
    isNameIndexed = False
    #Loop through all text to get each spell
    for i in range(0, len(list)):
        c = 5
        #Filter down searches so it exis asap
        if 'level' in list[i]:
            if list[i-1] == '-':
                if list[i-2][0].isdigit():
                    while(not isNameIndexed):
                        #Verify if spell legit
                        if not spellVerify(list[i:i+20]):
                            c+=1
                            break
                        #Check for empty line
                        if list[i-c] == ' ':
                            #Save
                            indexedLocations.append(i-c+1)
                            isNameIndexed = True
                        else:
                            c+=1
        #Check for cantrips
        elif 'cantrip' in list[i]:
            indexedLocations.append(i-1)
        isNameIndexed = False
    return indexedLocations

def arrayTheArray(list, indexList):
    arrayOfArrays = []
    #Setup array
    for i in range(1,len(indexList)):
        arrayOfArrays.append(list[indexList[i-1]:indexList[i]-1])
    arrayOfArrays.append(list[indexList[i]:])
    return arrayOfArrays

def spellFormat(array):
    pass


#Collect the PDFobject and set the file reader object
spellPDF = PyPDF2.PdfFileReader(open('../Spells.pdf', 'rb'))
#print(spellPDF.getPage(spellPDF.numPages - 1).extractText())
bigOlContent = pdfToList(spellPDF)
spellNameLocations = getSpellNamesIndex(bigOlContent)
spellArray = arrayTheArray(bigOlContent, spellNameLocations)
print(spellArray[-1])
#Print all da names
#for i in range(1, len(spellNameLocations)):
    #print(bigOlContent[spellNameLocations[i-1]:spellNameLocations[i]-1])
#print(bigOlContent)
