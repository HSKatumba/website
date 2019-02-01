#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:8
#Then, the output should be:40320


intr=int(input("Enter a single number: "))

def factorial(intr):
    if intr == 0:
        return 1
    else:
        return intr * factorial(intr-1)

print(factorial(intr))

