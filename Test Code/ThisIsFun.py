def fun(a):
    b=""
    for i in a:
        if (i=='a'or i=='e' or i=='i' or i=='o' or i=='u'):
            b+=i;
        elif i==' ':
            b+='';
        else:
            b+=i+'o'+i
    return (b)

if __name__== "__main__":
    print (fun("this is fun"))