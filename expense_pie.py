import matplotlib.pyplot as plt

def main():
    print()
    write_expense_file()
    expenses = read_expense_file()
    create_pie(expenses)


def write_expense_file():
    expense_file = open('expense.txt', 'w')
    
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
    expense_file.close()

def read_expense_file():
    expense_list = []
    expense_file = open('expense.txt', 'r')
    expense_list = expense_file.readlines()
    print(expense_list)

    index = 0
    while index < len(expense_list):
        expense_list[index] = expense_list[index].rstrip('\n')
        expense_list[index] = float(expense_list[index])
        
        index +=1
    print(expense_list)
    return expense_list

def create_pie(expenses):
    
    slice_labels = ['Rent', 'Gas', 'food', 'clothes', 'car payment', 'misc']

    plt.pie(expenses, labels=slice_labels)

    # Add a title.
    plt.title('Gastos ko')

    # Display the pie chart.
    plt.show()



main()