def main():
    years = int(input("eneter number of years"))
    compute_rainfall(years)

def compute_rainfall(years):
    total = 0
    for i in range(1, years+1):
        print(f"year number {i}")
        for month in range(1, 13):
            # rain_inches = float(input("enter rainfall measurement for month  " + str(i)))
            rain_inches = float(input(f"enter rainfall measurement for month  {month}: " ))
            total += rain_inches
        
        # total_rainfall += total
    print(f"total rainfall in inches is {total}")
    print(f"average rainfall in {years} years is {total/years}")


main()