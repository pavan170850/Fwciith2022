import numpy as np
import matplotlib.pyplot as plt
#from mpmath import cot
import cvxpy as cp
a=np.pi

#program to find maxima using  geometrical approaximation
#GP 2: Use 1 variable, approximate objective function
x = cp.Variable(pos="true", name="x")

#End point for iteration
delta = 0.001
error = 0.005
max_iter = 1000

#Initial guess
x.value = 1 
xk = x.value - 10*delta 

num_iter = 0
while(np.abs(x.value - xk) > delta and num_iter < max_iter):
    xk = x.value
    f_val = -a*xk**3 + 9*a*xk**2
    V = f_val * (x/xk) ** ((xk/f_val)*(-3*a*xk**2 + 18*a*xk))
    constraints = [x >= xk/(1+error) , x <= (1+error)*xk]
    prob = cp.Problem(cp.Maximize(V), constraints)
    if(prob.is_dgp() == False):
        print("Not DGP")
        break
    prob.solve(gp = True)
    num_iter += 1
    
print("Number iterations:", num_iter)
print("Max volume:", prob.value)
print("x=:", x.value)


#  Maxima using gradient ascent method.
def  f(x):
	return a*(x**2)*(9-x)

#For maxima using gradient ascent
cur_x = 2
gamma = 0.001 
precision = 0.00000001 
previous_step_size = 2 
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 3*a*x*(6-x)         

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += gamma  * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

print("Maximum value of f(x) is ",f(cur_x), "at","x =",cur_x)
#Plotting f(x)
x=np.linspace(0,10)
y=a*(x**2)*(9-x)
plt.plot(x,y,label='$V(x)=π(9x^2-x^3)$')

#Labelling points
plt.plot(cur_x,f(cur_x),'o')
plt.text(cur_x*(1+0.1), f(cur_x)*(1+0.02),'P(6,339)')

plt.grid()
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()





