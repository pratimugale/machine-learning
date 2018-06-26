import matplotlib.pyplot as plt

# Points to be plotted:
xdata = [50, 55, 56, 58, 45, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
ydata = [60, 54, 77, 74, 65, 75, 43, 65, 76, 73, 78, 63, 56, 83, 75, 85]

# To plot a line:
# y = mx + c
# y = theta0 + xtheta1

def lineplot(c, m):
    lineplotx = 100
    lineploty = (m*lineplotx)+c
    plt.plot([0, lineplotx], [c, lineploty])

# cf = cost function

lineplot(50, -2)

plt.plot(xdata, ydata, 'ro', markersize = 2)
plt.axis([0, 100, 0, 100])
plt.xlabel('X - AXIS')
plt.ylabel('Y - AXIS')
plt.show()
