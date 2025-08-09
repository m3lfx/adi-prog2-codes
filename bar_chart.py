import matplotlib.pyplot as plt

def main():
    # Create a list with the X coordinates of each bar's left edge.
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar.   
    heights = [100, 200, 300, 400, 500]
    bar_width = 5

    # Build the bar chart.
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'y', 'k'))

    # Display the bar chart.
    plt.show()

# Call the main function.
main()
