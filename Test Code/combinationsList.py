from itertools import combinations as comb
import timeit
count = [0]
def findComb(a,added):

    length = len (a)
    count[0] += 1

    for i in range(1,length+1):
        b = list(comb(a,i))
        for j in b:
            c = list(j)
            if sum(c) == added and count[0] == 1:
                print (c)
        

if __name__ == '__main__':
    #findComb([1,2,5,7,6], 10)
    timeTaken = timeit.Timer('findComb([1,2,3,4,5], 6)', 'from __main__ import findComb')
    print (min(timeTaken.repeat(3,100)))