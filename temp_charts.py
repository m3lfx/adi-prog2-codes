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
def write_temp_csv(filename, start, years):
    

def read_temp_csv(filename):

def create_graph():


main():