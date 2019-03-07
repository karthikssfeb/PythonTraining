def maxOfThree(a,b,c):
    if (a>b & a>c):
        return a;
    elif (b>a & b>c) :
        return b;
    elif (c>a & c>b) :
        return c;
if __name__ == "__main__":
    print ("The maximum of 3, 7 and 4 is %d" % max(3,4,7), "The End!", sep="\n")