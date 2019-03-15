print ({i:i**2 for i in range(6)})
print ([i**2 for i in range(6)])

def gen ():
    for i in range(1000):
        yield i**2
        i+=1

g = gen()
for i in range (6):
    print(next(g))