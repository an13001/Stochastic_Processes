from math import *
 

INF = -1000
N =    1000000


def Cumulative_Dist(d):
    a = (d-INF)/N
    n_d = 0.0
    for i in range(N):
        n_d += exp(-pow(INF + (i*a),2)/2)*a
    n_d = n_d/sqrt(2*pi)
    return n_d



def Call_Option(S,t,K,sigma,T,r):
    sqr_sigma = pow(sigma,2)/2
    T_t = T-t
    ln_ = log(S/K)
    d1 = (ln_ + (r + sqr_sigma)*T_t)/(sigma*sqrt(T_t))
    d2 = d1 - (sigma*sqrt(T_t))

    C = (S*Cumulative_Dist(d1)) - (K*exp(-r*T_t)*Cumulative_Dist(d2))
    return C

def Put_Option(S,t,K,sigma,T,r):
    sqr_sigma = pow(sigma,2)/2
    T_t = T-t
    ln_ = log(S/K)
    d1 = (ln_ + (r + sqr_sigma)*T_t)/(sigma*sqrt(T_t))
    d2 = d1 - (sigma*sqrt(T_t))

    P = (K*exp(-r*T_t)*Cumulative_Dist(-d2)) - (S*Cumulative_Dist(-d1))
    return P

#print(Cumulative_Dist(10))

print(Call_Option(50,0,100,0.25,1,0.05))
print(Put_Option(50,0,100,0.25,1,0.05))



 
