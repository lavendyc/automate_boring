def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-1)+ fabonacci(n-2)
    
print 'Please enter the value of n'
n = None
while True:
    if n != None:
        print 'Try again:'
    n=str(raw_input())
    if not n.isdigit():
        continue
    elif int(n)> 1000:
        continue
    elif int(n) < 0:
        continue
    else:
        break
print fabonacci(n)
