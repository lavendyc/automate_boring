print('Please enter the value of N:')
n=input()
x=1
while x == False:
    print('N should be a number between 1 and 1000, please try again.')
    n = str(input())
    if not isinstance(n,int):
        x = False
    elif int(n)<1 or int(n)>1000:
        x = False
    else:
        x = True
        if x == True:
            break
    
if int(n)>=1 and int(n)<=1000:
    i=1
    for s in range(0,int(n)):
        while i<10000:
            result = True
            i+=1
            for j in range(2,int(i**0.5)+1):
                if int(i)%j == 0:
                    result = False
            if result == True:
                print(str(i)+','),
                break

