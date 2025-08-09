import matplotlib.pyplot as plt

x_coords = [0, 1, 2, 3, 4,5]
y_coords = [0, 3, 1, 5, 2,10]
plt.title('Sample Data')
# Add labels to the axes.
plt.xlabel('This is the X axis')
plt.ylabel('This is the Y axis')

plt.xlim(xmin=-1, xmax=6)
plt.ylim(ymin=-1, ymax=11)

# Add a grid.
plt.grid(True)

plt.plot(x_coords, y_coords)
plt.show()



