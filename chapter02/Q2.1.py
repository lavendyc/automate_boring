def checkprime(n):
    d=2
    while d<=(n/2):
        if n%d==0:
            return 0
        d+=1
    return 1
 
 
def primeno(term):
    numbers=[]
    i=2
    while len(numbers)<term:
        if checkprime(i)==1:
            numbers.append(i)
        i+=1
    print (numbers)
print('Please enter the value of N:')
primeno(input())
