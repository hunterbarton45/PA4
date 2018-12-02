#problem #1
def gcd(a, b):  # takes two numbers as parameters
    if(b==0):  # base case to end recursion
        return a
    else:
        return gcd(b,a%b) #for example (10,5) gets put into this else statement. it returns gcd of (5,0) now
        # since b == 0 we return a which is 5, which is the gcd of (10,5)
a = int(input("Enter first integer for gcd: "))
b = int(input("Enter second integer for gcd: "))
print("GCD is: ", gcd(a, b))
print()


#problem #4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

myNum = int(input("please enter a integer for factorial: ")) #this will convert your number to a string. That is what input does
print("factorial of your number: ", factorial(int(myNum))) #you have to cast the variable myNum to an int


#problem #3
def sorted_array():
    #numbers list because Python doesn't have built in support for array's
    numbers = [1, 5, 3, 2, 4]

    # sort the numbers
    numbers.sort()
    return numbers

# print numbers in order
print('Sorted list: ', sorted_array())
