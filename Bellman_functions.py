'''

    Author: Rishab Lalwani
    Title: Q2 To Compute the true utility function and the best linear approximation

'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random as rand


fig = plt.figure()
ax = Axes3D(fig)
a = [x for x in range(1, 11)]
b= [x for x in range(1, 11)]
X, Y = np.meshgrid(a, b)
W=1

#A 10 × 10 world with a single +1 terminal state at (10,10)

Z = 1 - (11-X)*W - (11-Y)*W
n=9
m=9
Z[n][m] = 1

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='BuGn')
ax.set_xlabel('x_world')
ax.set_ylabel('y_world')
ax.set_zlabel('z_world')

#B As in (a), but add a −1 terminal state at (10,1).

Z[n][0] = -1

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='BuGn')
ax.set_xlabel('x_world')
ax.set_ylabel('y_world')
ax.set_zlabel('z_world')

l=list(range(1,10))

#3 As in (b), but add obstacles in 10 randomly selected squares.
# 10 Obstacles in Z
for i in range(10):
    Z[rand.choice(l)*W][rand.choice(l)*W] = rand.choice(l)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='BuGn')
ax.set_xlabel('x_world')
ax.set_ylabel('y_world')
ax.set_zlabel('z_world')


#4 As in (b), but place a wall stretching from (5,2) to (5,9).

wall_top=11
wall_bottom=6

if X.all()>=5:
    Z = 1 - (wall_top-X)*W - (wall_top-Y)*W
else:
    Z = 1 - (wall_bottom-X)*W - (wall_top-Y)*W - 5
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='BuGn')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#5 As in (a), but with the terminal state at (5,5).

each=5
Z = 1 - np.abs((each-X))*W - np.abs(each-Y)*W
Z[each][each] = 1

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='BuGn')
ax.set_xlabel('x_world')
ax.set_ylabel('y_world')
ax.set_zlabel('z_world')