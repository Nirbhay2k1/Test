import matplotlib.pyplot as plt
import numpy as np

#Problem 1
"""plt.figure(figsize = (5, 5))
plt.axhline(y = 7)
plt.show()"""
#Problem 2
"""plt.figure(figsize = (10, 5))
plt.axvline(x = 7)
plt.show()
"""

#problem 3
"""a=["A","B","C","D","E","F","G"]
b=[1,24,5,3,2,52,4]
col=["red","green","brown","black","grey","yellow","blue"]
plt.bar(a,b,color=col)
plt.show()"""

#problem 4
"""import matplotlib.pyplot as plt
X = range(1, 52)
Y = [value * 3 for value in X]
print(*range(1,50)) 
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()"""


#Problem 5
"""import matplotlib.pyplot as plt
with open("cord.txt") as f:
    data = f.read()
data = data.split('\n')
print(data)
x = [row.split(' ')[0] for row in data]
print(x)
xcod=[int(i) for i in x]
print(xcod)
y = [row.split(' ')[1] for row in data]
print(y)
ycod=[int(j) for j in y]
print(ycod)
plt.plot(xcod, ycod)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
"""
