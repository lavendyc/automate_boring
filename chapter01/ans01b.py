print('Enter the value of N:')
n=str(input())
print('Enter the value of L:')
l=int(input())
if(int(n)<0):
    print('ERROR')
elif(l>=len(n)):
    z='%0'+str(l)+'d'
    s=z%(int(n))
    print(s)
