# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:05:04 2017

@author: lcharleux
"""

import numpy as np # Clone de Matlab
import matplotlib.pyplot as plt # Librairie graphique

def fonction(x, tau, omega):
  """
  Une fonction à tracer.
  
  fonction(1,2,3) =  0.051915149703173388

  """
  return np.exp(-x / tau)*np.sin(omega * x)
  
# Tracé de la fonction
x = np.linspace(0., 10., 1000)   
y1 = fonction(x, tau = 5., omega = .5* np.pi)
y2 = fonction(x, tau = 3., omega = 2.* np.pi)
#-------------------------------------------------
# Mise en page plus fine de la figure
from matplotlib import rcParams
plt.rc('text', usetex=True) # Utiliser le c
plt.rc('font', family='serif', 
       weight='normal', style='normal')
#rcParams['font.serif'] = ['Palatino']
plt.rc('text.latex', preamble = 
    '''\usepackage[T1]{fontenc}
       \usepackage[bitstream-charter]{mathdesign}''')
rcParams['font.size']  =  10
rcParams["xtick.labelsize"] = 10.
rcParams["ytick.labelsize"] = 10.
rcParams['axes.labelsize'] = 10.
#rcParams['title.labelsize'] = 20.
width = 6.69 # Largeur de la figure
heigth = width /2.5 # Hauteur de la figure
#-------------------------------------------------
fig = plt.figure(figsize = (width, heigth))
plt.plot(x, y1, label = r"$\tau = 5, \omega = \pi/2 $")
plt.plot(x, y2, label = r"$\tau = 3, \omega = 2\pi $")
plt.grid()
plt.legend(loc = "best")
plt.xlabel("Temps, $t$")
plt.ylabel("Amplitude, $y(t)$")
plt.title(r"Oscillateur amorti: $y(t) = \exp(-t/\tau)\sin(\omega t)$")
#plt.show()
plt.tight_layout() # Spécifique qu'il faut ajuster la boite pour ne pas mordre sur les labels...
plt.savefig("oscillateur.pdf")