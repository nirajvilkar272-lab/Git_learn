import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# SUBPLOTS

# Syntaxes with explanation

# Subplots
# fig ,axs = plt.subplots(a,b) here a & b are the no. of graphs in x and y direction
#example
fig , axs = plt.subplots(2,2)
fig ,axs = plt.subplots(1,2)


# subplot variations
# fig, axs = plt.subplots(2,2, subplot_kw={'projection':'x'})
# x can be polar,3d,log(xscale,yscale)
# examples (practiced in jupyter notebook)
fig, axs = plt.subplots(2,2, subplot_kw={'projection':'polar'})
fig, axs = plt.subplots(1,1, subplot_kw={'projection':'3d'})
fig, axs = plt.subplots(1,1, subplot_kw={'xscale':'log', 'yscale':'log'})

# Subplot attr 
#  fig , axs = plt.subplots(a,b,figsize =(l,m),subplot_kw={$},gridspec_kw={%})

# gridspec_kw{%}
# here % is 'width_ratio': [x,y],'height_ratio':[x,y]

# subplot_kw{$}
# here $ has many types
# 1. Axis label {'xlabel':'X','ylabel':'Y'}
# 2. Aspect Ratio {'aspect':'equal'
# 3. Defining projection type {'projection' : 'polar'/'3d'/(xscale:'log',yscale:'log')

# Style
# loop over axis 
fig ,axs = plt.subplot(2,2, figsize = (8,6))
for ax in axs.flat:
    ax.plotss(x,np.sin(x),
              linestyle = '--',
              linewidth = 2,
              color = 'red',
              marker = 'o')


























