print('Please enter the value of N:')
n=input()
if n>=1 and n<=1000:
    s=1
    while s<=n:
        for i in range(2,10000):
            x=1
            for j in range(2,i/2):
                if i%j==0:
                    x=0
            if x==1:
                s=s+1
            print (str(i)+','),
            break
elif isinstance(n,str):
    print('N should be a number between 1 and 1000, please try again.')
else:
    print('N should be a number between 1 and 1000, please try again.')
