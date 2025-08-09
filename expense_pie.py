def main():
    print()
    write_expense_file()

def write_expense_file():
    expense_file = open('expense.txt', 'a')
    
    print('Enter data for expense #', sep='')
    rent = float(input('Rent Amount: '))
    gas = float(input('Gas: '))
    food = float(input('food: '))
    clothes = float(input('clothes: '))
    car_pay = float(input('car: '))
    misc = float(input('misc: '))

    # Write the data as a record to the file.
    expense_file.write(f"{rent}\n")
    expense_file.write(f"{gas}\n")
    expense_file.write(f"{food}\n")
    expense_file.write(f"{clothes}\n")
    expense_file.write(f"{car_pay}\n")
    expense_file.write(f"{misc}\n")

    # Display a blank line.
    print()
main()