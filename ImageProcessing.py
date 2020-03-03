#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Setareh Khoylow
"""

#%%
import numpy as np
import matplotlib.image as mpimg
#import matplotlib.pyplot as plt

#%% Q1
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')

heightA, widthA, d = a.shape
heightB, widthB, d = b.shape

top_val = int((heightA - heightB)/2)
bottom_val = int(heightB + top_val)
left_val = int((widthA - widthB)/2)
right_val = int(widthB + left_val)

c = a.copy()
c[top_val:bottom_val, left_val:right_val] = b

#plt.imshow(c)

mpimg.imsave("c.jpg", c)

#%% Q2
d = mpimg.imread('d.jpg')
e = mpimg.imread('e.jpg')

f = d.astype(np.float) - e.astype(np.float)
mask = (abs(f) < 50).all(axis=2)
f[mask] = 0
f = f.astype(np.uint8)

#plt.imshow(f)

mpimg.imsave("f.jpg", f)

#%% Q3
minion = mpimg.imread('g.jpg')
shugga = mpimg.imread('h.jpg')

target_color = minion[100,100]

i = minion.copy()
i = i.astype(np.float)
mask = (abs(i-target_color)<120).all(axis=2)
i[mask] = 0
i = i.astype(np.uint8)

heightM, widthM, d = minion.shape
heightS, widthS, d = shugga.shape

#move minion with black background to the shugga image
bottom_val = int(heightS) 
top_val = int(bottom_val - heightM)
left_val = int((widthS - widthM)/2)
right_val = int(widthM + left_val)

shugga_c = shugga.copy()
shugga_c[top_val:bottom_val, left_val:right_val][~mask] = i[~mask] #places the minion in the shugga image without the black background

#plt.imshow(shugga_c)

mpimg.imsave("i.jpg", shugga_c)