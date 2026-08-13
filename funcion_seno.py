#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:29:08 2026

@author: Sebastian Ceballes
"""

import numpy as np
import matplotlib.pyplot as plt # ¡Corrección 1: Faltaba el .pyplot!


#%% Definiciones

fs = 1000 # Hz
N = 1000  # Muestras

#%% Funciones

def mi_funcion_sen(vmax = 1, dc = 0, ff = 1, ph = 0, nn = N, fs = fs):
   # hasta acá
   return(a)


#%% Comienzo del script

vmax = 4
dc = 0
ff = 2
ph = 0

# np.arange crea los puntos desde 0 hasta (N/fs) con pasos de (1/fs)
vector_tiempo = np.arange(0, N/fs, 1/fs)

xx = vmax * np.sin(2 * np.pi * ff * vector_tiempo + ph) + dc


plt.plot(vector_tiempo, xx)
plt.grid(True) 
plt.show()