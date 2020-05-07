import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

height = 1000
width = 1000
n_map = np.zeros([height, width])

x_pos = math.floor(height/2)
y_pos = math.floor(width/2)
#start at the center of the grid
start = n_map[x_pos][y_pos]

start = 0.0

moves = ((0,-1),(-1,0),(1,0),(0,1))
dists = (0,1,3,5,7,10)
dprob = [(a*1)+0.01 for a in dists] 
for i in range(0,100000):
  choice = random.choices(moves, [0.25,0.25,0.25,0.25])[0]
  distance = random.choices(dists, dprob)[0]
  for ix in range(0,distance):
    x_pos += choice[0]
    y_pos += choice[1]
    try:
      n_map[x_pos][y_pos]+=random.choices([0,0.5,1,10,100],[0.05,0.05,0.8,0.09,0.01])  
    except Exception as ee:
      continue
      
plt.figure(figsize = (25,25))
plt.imshow(n_map, cmap="gist_earth", interpolation="bicubic") #hot
