def main():
    num_laps = int(input("enter number of laps"))
    lap_time(num_laps)

def lap_time(num_laps):
    ave_laps = 0
    largest = 0
    fastest = 1000
    for i in range(num_laps):
        time = float(input("enter your running time"))
        #largest input is 10

        #loop2 input is 4
        #loop3 input is 90
        if time > largest:
            largest = time
            #largest = 10


        #fastest time 
        # 10
        # 10 20 4
        if time < fastest:
            fastest = time
        ave_laps += time

    
    average = ave_laps / num_laps
    print("average lap times", average )
    print("the slowest time is: ", largest)
    print("the fastest time is: ", fastest)


main()