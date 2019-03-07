def isMember(elem, list):
    if elem in list:
        return True
    else:
        return False

if __name__ == "__main__":
    print ("Is the number 10 in the list [1,2,10,5] \n%s" % (isMember(10,[1,2,10,5])))