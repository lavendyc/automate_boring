def collatz(number):
    if number%2 == 0:
       return number//2
    elif number%2 == 1:
       return 3*number+1

try:
    print 'Enter a number:'
    number=input()
    while number != 1:
        number = collatz(number)
        print number
except ValueError:
    print('Please enter again.')
