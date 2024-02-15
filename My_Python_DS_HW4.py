#Lab3 - Write 5 Lines of Code Using Matplotlib, Multiple Plot Windows

#5.
import numpy as np
import matplotlib.pyplot as plt

# create a range for the x values using the arange() function
# from 0 to 1 with counts set to 81
x = np.linspace(0, 1, 81)

# Now create 3 functions of y with respect to x using the constant values a, b, c, and d.

print("First Function:\ny1(x) = x / sqrt(1 - x^2)\n")
y1 = x / np.sqrt( 1 - x**2)

print("Second Function:\ny2(x) = sqrt(1 - x^2) / x\n")
y2 = np.sqrt(1 - x**2) / x

print("Third Function:\ny3(x) = x / sqrt( 1 + x^2)\n")
y3 = x / np.sqrt(1 + x**2)

# Define the figure 1 plot
plt.figure(1)

# plot two subplots in a 2 x 1 window

# the 1st function is plot in black with circle points
ax1 = plt.subplot(211)
ax1.plot(x, y1, 'ko')

# the 2nd function is plot in yellow with dashed points
ax2 = plt.subplot(212)
ax2.plot(x, y2, 'y--')


# Now, Define the 2nd figure plot
plt.figure(2)

# plots only the 1st function here
plt.plot(x, y1)

# Now, Define the 3rd figure plot
plt.figure(3)

# plots the 3rd function here in magenta with cross points
plt.plot(x, y3, 'mx')

# Show all 3 plot figures here at the same time
plt.show()
