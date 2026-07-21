# Matplotlib Basics
import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3,4]
y = [10,20,30,35]
plt.plot(x,y) # Plots data 
plt.show()    # Shows/Displays data

# Figures and Axes
#Matplotlib hierarchy : fig>axes>plot elements
fig = plt.figure()                 # Create figure
ax = fig.add_subplot(111)          # Add one subplot (1 row, 1 col, index 1)
ax.plot([0, 1], [0, 1])            # Plot on this Axes
plt.show()

#Labels and Titles
plt.plot([1, 2, 3], [4, 3, 6])
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Line Plot")
plt.show()

#Legends
plt.plot([1, 2, 3], [1, 4, 9], label="Squares")
plt.plot([1, 2, 3], [1, 2, 3], label="Linear")
plt.legend()
plt.show()

#Colors,linestyle(customization)
plt.plot([1, 2, 3], [1, 4, 9], color="red", linestyle="--", marker="o")
plt.show()

# Scatter plot
x = [5, 7, 8, 7, 2, 17]
y = [99, 86, 87, 88, 100, 86]
plt.scatter(x, y, color="blue")
plt.show()

#Bar chart
categories = ["A", "B", "C"]
values = [3, 7, 5]
plt.bar(categories, values)
plt.show()

#Histogram
data = [1,1,2,3,3,3,4,4,5,5,5,5,6,7]
plt.hist(data, bins=5, color="green", edgecolor="black")
plt.show()

#Pie Chart
sizes = [15, 30, 45, 10]
labels = ["A", "B", "C", "D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()

# Grids
plt.plot([1, 2, 3], [1, 4, 9])
plt.grid(True)
plt.show()


# Sheet style
plt.style.use("classic") # plain, minimal style
plt.style.use("ggplot")  # grey background ,white grid
plt.style.use("seaborn") # soft blue theme
plt.style.use("fivethirtyeight") # grey background,bold lining,simple styling
plt.style.use("dark_background") # dark theme(black background)
plt.style.use("grayscale") # Grey background ,bold lining
plt.style.use("bmh") # clean modern look with dotted fade gridlines
plt.style.use("Solarize_Light2") # soft yellow background
plt.style.use("_mpl-gallery") # similar to solarsize ,bold lines

