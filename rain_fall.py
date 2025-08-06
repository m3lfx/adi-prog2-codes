def main():
    years = int(input("eneter number of years"))
    compute_rainfall(years)

def compute_rainfall(years):
    for i in range(1, years+1):
        # rain_inches = float(input("enter rainfall measurement for month  " + str(i)))
        rain_inches = float(input(f"enter rainfall measurement for month  {i}" ))


main()