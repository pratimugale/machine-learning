import matplotlib.pyplot as plt

# Points to be plotted (Dataset):
#xdata = [50, 55, 56, 58, 45, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
#ydata = [60, 54, 77, 74, 65, 75, 43, 65, 76, 73, 78, 63, 56, 83, 75, 85]
xdata = [10, 20, 30, 40, 50, 60, 70, 80, 90]
ydata = [40, 60, 40, 60, 40 ,60, 40, 60, 40]
m = len(xdata)

# To plot a line:
# y = mx + c
# y = theta0 + xtheta1

def linePlot(c, m):
    lineplotx = 100
    lineploty = (m*lineplotx)+c
    plt.plot([0, lineplotx], [c, lineploty])

def costFunctionCalculator(t0, t1):
    # cf = cost function
    # t0 = theta0
    # t1 = theta1
    # This is h(x) = theta0 + x(theta1)
    cfsum = 0
    for i in range (len(xdata)):
        diff = (t0 + ((xdata[i])*t1) - ydata[i])
        cfsum += diff*diff
    cf = cfsum/(2*len(xdata))
    return cf

def gradientDescentT0(t0, t1, lr):
    tempsum = 0
    for i in range (m):
        tempsum += (t0 + (xdata[i]*t1) - ydata[i])
    return (t0 - ((lr/m)*tempsum))

def gradientDescentT1(t0, t1, lr):
    tempsum = 0
    for i in range (m):
        tempsum += (t0 + (xdata[i]*t1) - ydata[i])*xdata[i]
    return (t1 - ((lr/m)*tempsum))



''' TRIAL
theta0 = 1
theta1 = 1
costFunction = costFunctionCalculator(theta0, theta1)
print ("Cost Function for y = x ===>", costFunction)
linePlot(1, 1)

costFunction = costFunctionCalculator(0, 1.1)
print ("Cost Function for y = 0 ===>", costFunction)
linePlot(0, 1.1)'''

# lr = learning rate (alpha)
slopealpha = 0.0000001
interceptalpha = 0.001
loops = 1500000
theta0 = 100
theta1 = 50

for i in range (loops):
    print ("Cost Function for Loop ", i, " ===> ", costFunctionCalculator(theta0, theta1))
    tempt0 = gradientDescentT0(theta0, theta1, interceptalpha)
    tempt1 = gradientDescentT1(theta0, theta1, slopealpha)
    print ("Slope of Best Fit Line       ===> "theta1)
    print ("Y-Intercept of Best Fit Line ===> "theta0)
    theta0 = tempt0
    theta1 = tempt1

linePlot(theta0, theta1)

plt.plot(xdata, ydata, 'ro', markersize = 2)
plt.axis([0, 100, 0, 100])
plt.xlabel('X - AXIS')
plt.ylabel('Y - AXIS')
plt.show()
