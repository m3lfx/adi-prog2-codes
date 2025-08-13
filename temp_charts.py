#create a program that will let the user enter a number of years and the monthly average temperature in celsius for 
# each year. the temperature data will be written to a file in a csv format. read the contents of
# the csv file and generate a line chart with the average of temperature for each year

import csv
import matplotlib.pyplot as plt

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
def main():
    start = int(input("Enter starting year   : "))
    years = int(input(f"Enter the number of years starting from {start}  : "))
    filename = "temp_data.csv"
    # write_temp_csv(filename, start, years)
    temp_years, ave_temps = average_temperature_per_year(filename)
    print(temp_years, ave_temps)
    create_line_chart(temp_years, ave_temps)

def write_temp_csv(filename, start, years):
    # print(filename, start, years)
    header = ["Year"] + MONTHS
    print(header)
    temperature_file = open(filename, 'w', newline='')
    print(" ".join(header) + "\n")
  
    temperature_file.write(" ".join(header) + "\n")
    writer = csv.writer(temperature_file)

    for i in range(years):
        year = start + i
        print(f"\nEntering data for Year {year}:")
        temps = []
        for month in MONTHS:
            temp = input(f"Enter temperature for {month}: ")
            temps.append(temp)
        print(temps)
        writer.writerow([year] + temps)
        print(f"\nData written to {filename}")
        temperature_file.close()
    # writer = csv.writer(temperature_file)
    # writer.writerow(header)
    

def average_temperature_per_year(filename):
    temperature_file = open(filename, 'r', newline='')
    
    reader = csv.reader(temperature_file)
    header = next(reader)  # Skip header
    # print(header)
    years = []
    temps = []
    avg_temp = []

    for row in reader:
        if not row or len(row) < 13:
            continue
        # print(row[1:])
        # print(row[0])
        years.append(row[0])

        for temp in row[1:]:
            # print(temp)
            temps.append(float(temp))
        avg = sum(temps) / len(temps)
        # print(temps)
        # print(avg)
        avg_temp.append(round(avg,2))
        print(avg_temp)

    return years, avg_temp
    

    # print(years)

def create_line_chart(years_label, temp_ave_data):
    plt.plot(years_label, temp_ave_data, linestyle='-', color='y', marker='o')
    plt.xlabel("Years")
    plt.ylabel("Average Temperature")
    plt.grid(True)
    plt.show()


main()