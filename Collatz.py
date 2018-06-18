def Collatz(number):

    if(number == 1):
        print(end='')
    elif (number % 2) == 0:
        number = number // 2
        print(number)
        Collatz(number)
    elif (number % 2) == 1:
        number = 3*number + 1
        Collatz(number)
    else:
        return

print("Enter an integer to implement the steps of the Collatz Conjecture")
number = int(input())
Collatz(number)