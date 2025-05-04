#create two arrays that are both filled with 1000 random numbers from a normal data distribution.

#The first array will have the mean set to 5.0 with a standard deviation of 1.0.

#The second array will have the mean set to 10.0 with a standard deviation of 2.0:

#Example
#A scatter plot with 1000 dots:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

#dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.

#We can also see that the spread is wider on the y-axis than on the x-axis.