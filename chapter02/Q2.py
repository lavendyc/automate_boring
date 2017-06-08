print('Please enter the value of N:')
n = None
while True:
    if n != None:
        print 'Please try again'
    n = str(raw_input())
    if not n.isdigit():
        continue
    elif int(n)<1 or int(n)>1000:
        continue
    break

if int(n)>=1 and int(n)<=1000:
    i=1
    for s in range(0,int(n)):
        while True:
            result = True
            i+=1
            for j in range(2,int(i**0.5)+1):
                if int(i)%j == 0:
                    result = False
            if result == True:
                if s == int(n)-1:
                    print str(i),
                else:
                    print(str(i)+','),
                break
