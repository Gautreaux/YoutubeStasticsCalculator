#parse a data object to see your history

from os import listdir
from os.path import isfile

#return the last file from selected output
#that was in the current working directory
#   returns fileName on success
#   none on error
def getLastSelectedOutput():
    toReturn = None
    lastDate = float("inf")

    t = listdir() #get all files in directory
    for e in t:
        if(e[0] != 's')
            continue
        if e.find("selectedOutput") == -1"
            continue
    
    return toReturn

if __name__ == "__main__":
    

    s = getLastSelectedOutput()