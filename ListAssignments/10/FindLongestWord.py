def findLongWordLength(wordList):
    lengthList = []
    for word in wordList:
        lengthList.extend([len(word)])
    return max(lengthList)

if __name__ == "__main__":
    namelist = ['karthick','satheesh','jaishankar']
    print("Longest in the list ['karthick','satheesh','jaishankar'] is %d" % findLongWordLength(namelist))