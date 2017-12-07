import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)  # s = size of dot c = color
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)  # s = size of dot c in rgb
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)  # using color map on Y values

# set chart title and labels
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# sets the range of each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')  # saves file to save directory and trims white space
