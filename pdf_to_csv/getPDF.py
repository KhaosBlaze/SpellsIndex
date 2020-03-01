import PyPDF2
from getPDF_functions import *
from classes.spell import *

def indexSpellOptions(array):
    """
    Indexed Array of spell template for parsing
        0 = Level
        1 = 'Casting Time:'
        2 = 'Range:'
        3 = 'Components:'
        4 = 'Duration'
        5 = 'End of Duration'
    """
    #Set Blank index
    index = [0]*6
    #Get index of 'level' with index
    for i in range(1, len(array)):
        if 'level' in array[i]:
            index[0] = i
            break
    index[1] = array.index('Casting Time:')
    index[2] = array.index('Range:')
    index[3] = array.index('Components:')
    print(index[3])
    index[4] = array.index('Duration:')
    return index

def textBetween(array, match):
    """
    Get the content between two indexes of an array and then strip the content
    for spaces, or just remove the match from the first string.
    """
    if array[0] != match:
        return array[0].split(' ')[-1]
    else:
        return ''.join(array[1:]).strip()

def stripPage(array):
    """
    Remove Page numbers from spell entries
    """
    try:
        pageLocation = array.index('Page ')
        array.pop(pageLocation)
        array.pop(pageLocation)
        return array
    except ValueError:
        return array


def spellFormat(array):
    """
    Format spells from an Array to the Spell class so the array of arrays can
    be iterated over and the array of Spell objects can have the option to print
    a csv formatted text.
    """
    spellTemplate = Spell()
    #Strip page numbers
    array = stripPage(array)
    #Get Index of key indicators from array of text for the spell
    index = indexSpellOptions(array)
    #Get name of spell from the start of the array to before the numeric level
    spellTemplate.name = ''.join(array[:index[0]-2]).strip()
    #Get the spell level (2 before the word level)
    spellTemplate.level = array[index[0]-2][0]
    spellTemplate.school = textBetween(array[index[0]:index[1]-1], 'level')
    spellTemplate.casting_time = textBetween(array[index[1]:index[2]-1],
                                                'Casting Time:')
    spellTemplate.range = textBetween(array[index[2]:index[3]-1], 'Range:')
    spellTemplate.components = textBetween(array[index[3]:index[4]-1],
                                                'Components:')
    spellTemplate.duration = array[index[4]+2]
    spellTemplate.Description = ''.join(array[index[4]+3:]).strip()
    #spellTemplate.duration = textBetween(array[index[4]:index[5]-1], 'Duration:')
    return spellTemplate

#Testing Variables
endingPage = 26
spellNumber = 3

#Collect the PDFobject and set the file reader object
spellPDF = PyPDF2.PdfFileReader(open('../Spells.pdf', 'rb'))
#print(spellPDF.getPage(spellPDF.numPages - 1).extractText())
bigOlContent = pdfToList(spellPDF, endingPage)
#Get index of where each spell starts
spellNameLocations = getSpellNamesIndex(bigOlContent)
spellArray = arrayTheArray(bigOlContent, spellNameLocations)

print(spellArray[spellNumber])
test = spellFormat(spellArray[spellNumber])
print(test)


#Print all da names
#for i in range(1, len(spellNameLocations)):
    #print(bigOlContent[spellNameLocations[i-1]:spellNameLocations[i]-1])
#print(bigOlContent)
