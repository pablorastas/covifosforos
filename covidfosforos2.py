# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:03:43 2020

@author: pablorastas
"""
from matplotlib import pyplot as plt
import matplotlib.animation as animation


import numpy as np
import time
import matplotlib.pyplot as plt
import numpy as np

d = 7
lado = 300
matriz1 = np.zeros((lado,lado))
matriz1 = matriz1.astype(int)

def propagar(matriz):
        a=np.copy(matriz)
        
        
    
        for e in  range(lado-1):
            
            for i in range(lado-1):
               
                    if   matriz[e][i] == 1 :
                        a[e][i] =-1
                        print(a[e][i],e,i)
                        if  e!=0 and i!=0 and a[e-1][i-1]!=-1 :
                       
                              a[e-1][i-1]=1
                        if  i!=0 and a[e][i-1]!=-1:
                              a[e][i-1]=1
                        if e!=0 and a[e-1][i] !=-1:
                              a[e-1][i]=1
                        if  a[e+1][i+1]!=-1  and  e!=lado-1 and   i!=lado-1:
                              a[e+1][i+1]=1
                        if  a[e][i+1]!=-1  and  e!=lado-1 and   i!=lado-1:
                              a[e][i+1]=1
                        if  a[e+1][i]!=-1  and  e!=lado-1 and   i!=lado-1:
                            a[e+1][i]=1
                        if  a[e+1][i-1]!=-1  and  e!=lado-1 and   i!=0:
                            a[e+1][i-1]=1
                        if  a[e-1][i+1]!=-1  and  e!=0 and   i!=lado-1:
                            a[e-1][i+1]=1
        return a
                
                       
                       
        
        

def ciclos(d):
   matriz=matriz1
   
   while d!=0:
       
        
        d=d-1
        
        matriz =propagar(matriz)
        print(matriz)
        c=np.argwhere(matriz == 1).transpose()
        b=np.argwhere(matriz == 0).transpose()
        e=np.argwhere(matriz == -1).transpose()
        
        plt.clf()
        plt.scatter(c[0],c[1], s=10,c='b' )
        plt.scatter(b[0],b[1], s=5,c='r' )
        plt.scatter(e[0],e[1], s=5,c='k' )
        plt.show()
        plt.pause(1)
        np.random.shuffle(matriz.flat)
        
       
   


matriz1[10][10]=1



ciclosc=ciclos(d)
