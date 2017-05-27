print('Enter the value of N:')
n=str(input())
print('Enter the value of L:')
l=int(input())
if(int(n)<0):
      print('ERROR')
elif(l>=len(n)):
      z='0'*(l-len(n))+n
      print(z)
