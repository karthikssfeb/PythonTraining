def isOverlapping(list1, list2):
    result = False
    for elem in list1:
        if elem in list2:
            return True
    else:
        return False


if __name__ == "__main__":
    print ( "is the list [1,2,3,4,5] overlapping with [8,5,10] \n%s" % isOverlapping([1,2,3,4,5],[8,5,10]))
