def main():
    num_loop = int(input("enter size of list"))
    num_list = []
    for num in range(num_loop):
        number = float(input("enter a number between 0 and 100"))

        while number < 0 or number > 100:
            print("invalid number")
            number = float(input("enter a number between 0 and 100"))
        
        num_list.append(number)
       
    
    total = sum(num_list)
    average = total / len(num_list)

    print(f"total is {total}")
    print(f"average is {average}")
main()