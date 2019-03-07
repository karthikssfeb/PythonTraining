def listMultiply(inputList):
    product=1
    for elem in inputList:
        product *=elem
    return product

if __name__ == "__main__":
    print ("The product of elements list [1,2,3,4] is %d " % listMultiply([1,2,3,4]))