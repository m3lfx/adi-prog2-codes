def main():
    num_list = []
    for i in range(1, 21):
        num = int(input(f"enter number {i}: "))
        num_list.append(num)
    
    print(f"lowest number {min(num_list)}")
    print(f"largest number {max(num_list)}")
    print(f"total numbers is {sum(num_list)}")  
    print(f"the average of the list of number is {sum(num_list) / len(num_list)}")
main()