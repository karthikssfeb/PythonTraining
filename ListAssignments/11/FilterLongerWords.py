def filterLongerWords (wordlist, length):
    filteredList = []
    for word in wordlist:
        if len(word) > length:
            filteredList.extend([word])
    return filteredList

if __name__ == "__main__":
    namelist = ["karthick","Yogesh","Jaishankar"]
    size = 6
    print ("Filtering the list %s for words longer than %d, the output is" % (namelist,size) ,filterLongerWords(namelist,size))