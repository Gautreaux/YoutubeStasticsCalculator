#parse a data object to see your history

from os import listdir
from os.path import isfile
import time
from html.parser import HTMLParser

#return the last file from selected output
#that was in the current working directory
#   returns fileName on success
#   none on error
def getLastSelectedOutput():
    toReturn = None
    lastDate = 0

    t = listdir() #get all files in directory
    for e in t:
        if e.find("selectedOutput") == -1:
            continue
        
        #so this is a valid file, but is it the most recent?
        #get the timestamp
        n = float(e[15:len(e)-5])
        if(n > lastDate):
            lastDate = n
            toReturn = e

    return toReturn



#inPath - path to the file containing parse ready data
# outPath - path to the output file
#output is formatted as follows:
#   one video per line: "<youtube id> <video length>"
def parseVideoData(inPath, outPath):
    ctr = 0


    start_time = time.time()
    with open(inPath, 'r', encoding='utf8') as inFile:

    print(ctr)
    print("Simple Parsing concluded in " + str(round(time.time()-start_time, 2)) + " seconds.")
    

if __name__ == "__main__":
    

    s = getLastSelectedOutput()
    print("Loading file: " + str(s))
    parseVideoData(s, 'parsedOutput')