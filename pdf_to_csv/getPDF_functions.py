import PyPDF2
from classes.spell import *

def pdfToList(pdfObj, lastPage):
    """Converts PDF object into a list of strings based off newline char"""
    #Take in a pdf object and output a list of all lines pdfObj.numPages
    bigList = []
    for i in range(24, lastPage):
        #Store page temporarily and convert to text and split to an array
        page = pdfObj.getPage(i)
        pageText = page.extractText()
        listPlaceholder = pageText.split('\n')
        #Add Array to big array
        bigList += listPlaceholder
    return bigList

def spellVerify(text):
    """Returns whether the text is actually a spell"""
    return 'Casting Time:' in text and 'Range:' in text


def getSpellNamesIndex(list):
    """
    Loops through pdf list of strings to get an index of locations of
    where the name of each spell is.
    """
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
                if list[i-2][0].isdigit() or list[i-3][0].isdigit():
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
    """Uses the index of name locaitons on list of text to create an array of
        string arrays so each item in the returned list is a spell to be parsed
        """
    arrayOfArrays = []
    #Setup array
    for i in range(1,len(indexList)):
        arrayOfArrays.append(list[indexList[i-1]:indexList[i]-1])
    arrayOfArrays.append(list[indexList[i]:])
    return arrayOfArrays

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
