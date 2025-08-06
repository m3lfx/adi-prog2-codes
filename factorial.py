import math
def main():
    number = int(input("enter an integer"))
    while number < 0:
        print("negative input")
        number = int(input("enter an integer"))

    if number > 0:
        factorial(number)
    num_fact = math.factorial(number)
    print(num_fact)
def factorial(number):
    sum = 1
    for i in range(1, number + 1 ):
        sum *= i
    print(f"the factorial of {number} is {sum}")

main()