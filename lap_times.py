def main():
    num_laps = int(input("enter number of laps"))
    lap_time(num_laps)

def lap_time(num_laps):
    ave_laps = 0
    for i in range(num_laps):
        #largest


        time = float(input("enter your running time"))
        ave_laps += time

    
    average = ave_laps / num_laps
    print("average lap times", average )


main()