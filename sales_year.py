import matplotlib.pyplot as plt

def main():
    # Create lists with the X and Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4, 5,6]
    y_coords = [0, 1, 2, 3,4,5,3]

    # Build the line graph.
    plt.plot(x_coords, y_coords, marker='v')

    # Add a title.
    plt.title('Sales by Year')

    # Add labels to the axes.
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick marks.
    plt.xticks(x_coords, ['2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.yticks(y_coords, ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m','$3m'])

    # Add a grid.
    plt.grid(True)

    # Display the line graph.
    plt.show()

# Call the main function.
main()