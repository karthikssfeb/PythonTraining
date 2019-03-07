def findWordLength(wordList):
    lengthList = []
    for word in wordList:
        lengthList.extend(len(word))
    return lengthList

def mapWordList(wordList,lengthList):
    wordList = lengthList

abc="abc"
sss="sss"
names = [abc,sss]
values = findWordLength(names)
mapWordList(tuple(names),values)
print (names)
