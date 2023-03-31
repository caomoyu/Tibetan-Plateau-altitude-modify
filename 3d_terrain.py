# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:05:18 2023

@author: caoyeer
"""


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from matplotlib import cm
from matplotlib.colors import LightSource
import salem


plt.rcParams.update({"font.size":20})
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
plt.close()




f1 = "./geo_em.d01.nc"
f2 = "./wrfinput_d01"
ds1 = xr.open_dataset(f1)
ds2 = xr.open_dataset(f2)
h1 = ds1.HGT_M.data[0,:,:]
h2 = np.where(h1>500,500,h1)



x = np.arange(0,109,1)
y = np.arange(0,109,1)
X,Y = np.meshgrid(x, y)
Z1 = h1
Z2 = h2



fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(221,projection='3d')
ls = LightSource(270, 20) 
rgb = ls.shade(Z1, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')


surf = ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, facecolors=rgb,
                        linewidth=0, antialiased=False, shade=False)
ax.set_title('(a)')
ax.set_zlim(0,6000)
ax.set_zlabel('m')




ax = fig.add_subplot(222,projection='3d')
ls = LightSource(270, 20) 
rgb = ls.shade(Z1, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, facecolors=rgb,
                        linewidth=0, antialiased=False, shade=False)
ax.set_title('(b)')
ax.set_zlim(0,6000)
ax.set_zlabel('m')
ax.view_init(elev=45., azim=0)





ax = fig.add_subplot(223,projection='3d')
ls = LightSource(270, 20)
rgb = ls.shade(Z2, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, facecolors=rgb,
                        linewidth=0, antialiased=False, shade=False)
ax.set_title('(c)')
ax.set_zlim(0,6000)
ax.set_zlabel('m')


ax = fig.add_subplot(224,projection='3d')
ls = LightSource(270, 20)
rgb = ls.shade(Z2, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(X, Y, Z2, rstride=2, cstride=1, facecolors=rgb,
                        linewidth=0, antialiased=False, shade=False)
ax.set_title('(d)')
ax.set_zlim(0,6000)
ax.set_zlabel('m')
ax.view_init(elev=45., azim=0)
plt.show()  
plt.subplot_tool()