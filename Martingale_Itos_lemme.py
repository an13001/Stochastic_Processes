import numpy as np
import matplotlib.pyplot as plt
from math import *
import random
#-------------- Macros --------------
T = 1
N = 20
Nme = 50
K = 50
delta_t = T/N
Nme = 200
sigma = 3
P = 1/2
S0 = 5
D = 1.5
U = 0.5
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

#Espérance du processus stochastique 0
def Esp_Stochastic_Process(t,n):
    esp = 0
    for i in range(Nme):
        esp += Create_Stochastic_Process(t,n)
    esp = esp/Nme
    return esp

#Variance du processus stochastique 0
def Var_Stochastic_Process(t,n):
    Var = 0
    for i in range(Nme):
        Var += pow(Create_Stochastic_Process(t,n),2)
    Var = Var/Nme
    return Var

#Processus stochastique 0 avec filtration
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

#Processus stochastique 1 avec filtration
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

#Processus stochastique 2 avec filtration
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


#------------------ Integrale Stochastique --------------------------------------

def Create_Integ_Stoch_Tab(t,n,nme):
    S=0
    L1=[]
    for j in range(nme):
        L = Create_Stochastic_Process_Tab(t,n)
        for i in range(n-1):
            S += exp(t*i)*(L[i+1]-L[i])
        L1 += [S]
    return L1

#--------------------------------------------------------------------------------

#----------- Random Walk -----------------------------------

def Marche_aleatoire(n):
    S=0
    L=[]
    for i in range(n):
        if random.randint(0,1) == 1:
            S += -1
        else:
            S += 1
        L += [S]
    return L

#-----------------------------------------------------------



#---------------- Random walk Martingale ------------------------------

def Martingal_MA(L,n):
    L1 = []
    for i in range(len(L)):
        L1 += [L[i]]
    S = L1[len(L1)-1]
    for i in range(n-len(L)):
        if random.randint(0,1) == 1:
            S += -1
        else:
            S += 1
        L1 += [S]
    return L1
        
    

#----------------------------------------------------------------------

#------------- Arbre binomial ------------------------

def Arbre_bin(u,d,p,n,s0):
    L = [s0]
    S = s0
    for i in range(n-1):
        if random.random() > p:
            S = S*u
        else:
            S = S*d
        L += [S]
    return L

#-----------------------------------------------------


"""

#-------------- Graphes ---------------------------#
----------------------------------------------------



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



#------------------------- Stochastic process 0 martingale ? ----------------------


L = Create_Stochastic_Process_Tab(delta_t,K)
S2 = 0
for i in range(1000):
    S2 += Filtration_Stochastic_Process(L,delta_t,N)[N-1]
S2 = S2/1000
S1 = Filtration_Stochastic_Process(L,delta_t,N)[K-1]
print(S1)
print(S2)

#----------------------------------------------------------------------------------

#----------------- Stochastic process 1  -----------------------------------------


for i in range(30):
    plt.plot( Create_X_Axe(delta_t,N), Create_Stochastic_Process_Tab_1(delta_t,N))
plt.show() 

#-------------------------------------------------------------------------------

#-------------- Stochastic process 1 with filtration --------------------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
for i in range(100):
    plt.plot( Create_X_Axe(delta_t,N), Filtration_Stochastic_Process_1(L,delta_t,N))
plt.show() 

#----------------------------------------------------------------------------------


#------------------------- Stochastic process 1 martingale ? ----------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
S2 = 0
for i in range(1000):
    S2 += Filtration_Stochastic_Process_1(L,delta_t,N)[N-1]
S2 = S2/1000
S1 = Filtration_Stochastic_Process_1(L,delta_t,N)[K-1]
print(S1)
print(S2)


#----------------------------------------------------------------------------------
#----------------- Stochastic process 2  -----------------------------------------

for i in range(30):
    plt.plot( Create_X_Axe(delta_t,N), Create_Stochastic_Process_Tab_2(delta_t,N,sigma))
plt.show() 

#-------------------------------------------------------------------------------

#-------------- Stochastic process 2 with filtration --------------------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
for i in range(50):
    plt.plot( Create_X_Axe(delta_t,N), Filtration_Stochastic_Process_2(L,delta_t,N,sigma))
plt.show() 

#----------------------------------------------------------------------------------



#------------------------- Stochastic process 2 martingale ? ----------------------

L = Create_Stochastic_Process_Tab(delta_t,K)
S2 = 0
for i in range(10000): 
    S2 += Filtration_Stochastic_Process_2(L,delta_t,N,sigma)[N-1]
S2= S2/10000
S1= Filtration_Stochastic_Process_2(L,delta_t,N,sigma)[K-1]
print(S1)
print(S2)

#----------------------------------------------------------------------------------



#----------------- Variation quadratique  -----------------------------------------

plt.plot( Create_X_Axe(delta_t,N), Create_Stochastic_Process_Tab(delta_t,N))
for i in range(2):
    plt.plot( Create_X_Axe(delta_t,N), Create_Quad_Var_Tab(delta_t,N)) 
plt.plot( Create_X_Axe(delta_t,N), Create_X_Axe(delta_t,N))
plt.show() 

#----------------------------------------------------------------------------------

#----------------- Integrale stochastique  -----------------------------------------


plt.plot( Create_X_Axe(delta_t,Nme), Create_Integ_Stoch_Tab(delta_t,N,Nme))
plt.show() 

#-------------------------------------------------------------------------------


#----------------- Esperance de l'integrale stochastique -----------------------

L2 = Create_Integ_Stoch_Tab(delta_t,N,Nme)
S =0
for i in range(len(L2)):
    S += L2[i]
print(S/len(L2))

#-------------------------------------------------------------------------------


print(len(Create_X_Axe(delta_t,N)))
print(len(Create_Integ_Stoch_Tab(delta_t,N)))



#--------------------- Random walk graph ----------------------------------

for i in range(10):
    plt.plot(Create_X_Axe(delta_t,N),Marche_aleatoire(N)) 
plt.show()

#--------------------------------------------------------------------------


#----------------------- Martingal Random walk ---------------------------
L = Marche_aleatoire(K)
for i in range(10):
    plt.plot(Create_X_Axe(delta_t,N),Martingal_MA(L,N))
plt.show()
#-------------------------------------------------------------------------
"""

#----------------------- Arbre binomial ---------------------------
for i in range(10):
    plt.plot(Create_X_Axe(delta_t,N),Arbre_bin(U,D,P,N,S0))
plt.show()
#-------------------------------------------------------------------------


