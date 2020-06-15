import math
print('Welcome to the Factor Generator App')
generator = True
#while loop
while generator:
    num = int(input('Enter a number to determine all factors of that number: '))
    factors = []
    for i in range(1, num+1):
        if num%i ==0:
            factors.append(i)
        else:
            continue
    print('\nFactors of ' + str(num) + ' are: ')
    for factor in factors:
        print(factor)
    print('\nIn summary: ')
    fact= int(len(factors)/2)
    for i in range(fact):
        print(str(factors[i]) + '*' + str(factors[-i-1]))
    #ask the user if they want to run the program again
    choice = input('\nRun again(y/n): ').lower()
    if choice !='y':
        #commented out is another way of writing it
        #print('Thank you for using the program. Have a great day. ')
        #break
        generator= False
        print('Thank you for using the program. Have a great day. ')
