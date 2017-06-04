print('Please enter the value of N:')
n = str(input())
if not n.isdigit():
    print('N should be a number between 1 and 1000, please try again.')
elif int(n)>=1 and int(n)<=1000:
    i = 2
    for s in range(0,int(n)):
        while i<10000:
            result = True
            for j in range(2,int(i**0.5)+1):
                if int(i)%j == 0:
                    result = False
            if result == True:
                print(str(i)+','),
            i+=1
            break
else:
    print('N should be a number between 1 and 1000, please try again.')
