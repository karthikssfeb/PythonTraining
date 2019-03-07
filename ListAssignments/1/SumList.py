def sumList(inputList):
    sum=0
    for elem in inputList:
        sum +=elem
    return sum

if __name__ == "__main__":
    print ("The Sum of list [1,2,3] is %d " % sumList([1,2,3]))