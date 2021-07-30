from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import time

plt.style.use('fivethirtyeight')

xVal = []
yVal = []


def animate(y):
    
    global x
    x = 1
    
    if y == 0:
        quit()
    while True:
        if y != 1:
            if y%2 == 0:
                y = y // 2
            else:
                y = y*3 + 1
            x += 1
            xVal.append(x)
            yVal.append(y)
            print(x,y)
            
        else:
            break


y = int(input("enter a number : "))
animate(y)
plt.tight_layout()
plt.title("3n+1 graph")
plt.plot(xVal,yVal)
plt.show()