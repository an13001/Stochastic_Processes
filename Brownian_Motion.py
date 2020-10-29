import numpy as np
import matplotlib.pyplot as plt
from math import *

#-------------- Macros --------------
T = 1 
N = 200
K = 50
delta_t = T/N
Nme = 200
sigma = 3
#------------------------------------


#--------------------------- Brownian Motion 0  -----------------------------------

def Create_Stochastic_Process(t,n):
    W=0
    sqrt_t = sqrt(t)
    for i in range(n):
        W += sqrt_t*np.random.randn(1)[0]
    return W
    

def Create_Stochastic_Process_Tab(t,n):
    L = []
    W = 0
    sqrt_t = sqrt(t)
    for i in range(n):
        L += [W]
        W += sqrt_t*np.random.randn(1)[0]
    return L

def Create_X_Axe(t,n):
    L = []
    for i in range(n):
        L += [i*t]
    return L


def Esp_Stochastic_Process(t,n):
    esp = 0
    for i in range(Nme):
        esp += Create_Stochastic_Process(t,n)
    esp = esp/Nme
    return esp

def Var_Stochastic_Process(t,n):
    Var = 0
    for i in range(Nme):
        Var += pow(Create_Stochastic_Process(t,n),2)
    Var = Var/Nme
    return Var

def Filtration_Stochastic_Process(L,t,n):
    L1 = [] 
    sqrt_t = sqrt(t)
    for i in range(len(L)):
        L1 += [L[i]]
    W = L[len(L)-1]
    for i in range(n-len(L)):
        W += sqrt_t*np.random.randn(1)[0]
        L1 += [W]
    return L1

#---------------------------------------------------------------------------------


#--------------- Brownian Motion 1 -----------------------------------------------


def Create_Stochastic_Process_1(t,n):
    W=0
    sqrt_t = sqrt(t)
    for i in range(n):
        W += sqrt_t*np.random.randn(1)[0]
    W = pow(W,2)
    W = W - delta_t*n
    return W


def Create_Stochastic_Process_Tab_1(t,n):
    L = Create_Stochastic_Process_Tab(t,n)
    for i in range(len(L)):
        L[i] = pow(L[i],2) - (delta_t*i)
    return L

def Filtration_Stochastic_Process_1(L,t,n):
    L1 = Filtration_Stochastic_Process(L,t,n)
    for i in range(len(L1)):
        L1[i] = pow(L1[i],2) - (delta_t*i)
    return L1
    

#---------------------------------------------------------------------------------

#--------------- Brownian Motion 2 -----------------------------------------------



def Create_Stochastic_Process_2(t,n,sigma):
    W=0
    sqrt_t = sqrt(t)
    for i in range(n):
        W += sqrt_t*np.random.randn(1)[0]
    W = exp(sigma*W - ((sigma_sqr*delta_t*i)/2))
    return W


def Create_Stochastic_Process_Tab_2(t,n,sigma):
    L1 = Create_Stochastic_Process_Tab(t,n)
    sigma_sqr = pow(sigma,2)
    for i in range(len(L1)):
        L1[i] = exp(sigma*L1[i]-((sigma_sqr*delta_t*i)/2))
    return L1

def Filtration_Stochastic_Process_2(L,t,n,sigma):
    L1 = Filtration_Stochastic_Process(L,t,n)
    sigma_sqr = pow(sigma,2)
    for i in range(len(L1)):
        L1[i] = exp(sigma*L1[i]-((sigma_sqr*delta_t*i)/2))
    return L1

#--------------------------------------------------------------------------------

#------------------- Variation quadratique ---------------------------------------

def Create_Quad_Var_Tab(t,n):
    L = Create_Stochastic_Process_Tab(t,n)
    L1 = [0]
    W = 0
    for i in range(len(L)-1):
        W += pow(L[i+1]-L[i],2)
        L1 += [W]
    return L1

#print(Create_Quad_Var_Tab(delta_t,N))
#---------------------------------------------------------------------------------



"""

#-------------- Stochastic process with filtration --------------------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
for i in range(50):
    plt.plot( Create_X_Axe(delta_t,N), Filtration_Stochastic_Process(L,delta_t,N))
plt.show() 

#----------------------------------------------------------------------------------


#------- Variance et Esperance ---------

print(Var_Stochastic_Process(delta_t,N))
print(Esp_Stochastic_Process(delta_t,N))

#---------------------------------------



#----------------- Stochastic process 0  -----------------------------------------

for i in range(10):
    plt.plot( Create_X_Axe(delta_t,N), Create_Stochastic_Process_Tab(delta_t,N))
plt.show() 

#-------------------------------------------------------------------------------


#----------------- Stochastic process 1  -----------------------------------------

for i in range(10):
    plt.plot( Create_X_Axe(delta_t,N), Create_Stochastic_Process_Tab_1(delta_t,N))
plt.show() 

#-------------------------------------------------------------------------------



#-------------- Stochastic process 1 with filtration --------------------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
for i in range(50):
    plt.plot( Create_X_Axe(delta_t,N), Filtration_Stochastic_Process_1(L,delta_t,N))
plt.show() 

#----------------------------------------------------------------------------------



#----------------- Stochastic process 2  -----------------------------------------

for i in range(10):
    plt.plot( Create_X_Axe(delta_t,N), Create_Stochastic_Process_Tab_2(delta_t,N,sigma))
plt.show() 

#-------------------------------------------------------------------------------


#-------------- Stochastic process 2 with filtration --------------------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
for i in range(50):
    plt.plot( Create_X_Axe(delta_t,N), Filtration_Stochastic_Process_2(L,delta_t,N,sigma))
plt.show() 

#----------------------------------------------------------------------------------

#----------------- Variation quadratique  -----------------------------------------

plt.plot( Create_X_Axe(delta_t,N), Create_Quad_Var_Tab(delta_t,N)) 
plt.plot( Create_X_Axe(delta_t,N), Create_X_Axe(delta_t,N))
plt.show() 

#----------------------------------------------------------------------------------

"""
