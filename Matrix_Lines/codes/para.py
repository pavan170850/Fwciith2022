import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as  LA

import sys  #for path to external scripts
sys.path.insert(0,'/sdcard/FWCmodule1/Matrix_Lines/codes/CoordGeo') #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex


r=5
b=4
K=3 #for ratio line dividing
theta= np.pi/3

A=r*np.array(([np.cos(theta),np.sin(theta)]))
B=np.array(([0,0]))
e1=np.array(([1,0]))
C=b*e1 #for base of triangle
D=A+C-B


#points P and Q

P=(B+K*D)/(K+1)
Q=(D+B*K)/(1+K)

#generating all lines

X_AB=line_gen(A,B)
X_BC=line_gen(C,B)
X_CD=line_gen(C,D)
X_DA=line_gen(D,A)
X_BD=line_gen(B,D) #DIAGONAL BD
X_AQ=line_gen(A,Q)
X_AP=line_gen(A,P)
X_QC=line_gen(Q,C)
X_PC=line_gen(P,C)
#plotting all lines

plt.plot(X_AB[0,:],X_AB[1,:])
plt.plot(X_BC[0,:],X_BC[1,:])
plt.plot(X_CD[0,:],X_CD[1,:])
plt.plot(X_DA[0,:],X_DA[1,:])
plt.plot(X_BD[0,:],X_BD[1,:])
plt.plot(X_AQ[0,:],X_AQ[1,:])
plt.plot(X_AP[0,:],X_AP[1,:])
plt.plot(X_QC[0,:],X_QC[1,:])
plt.plot(X_PC[0,:],X_PC[1,:])

#Direction vectors
m_1 = A-B
m_2 = C-B
m_3 = D-C
m_4 = D-A
m_5 = Q-B
m_6 = D-P

n_1 = A-P
n_2 = C-Q
n_3 = A-Q
n_4 = C-P

#norm

N1 = np.linalg.norm(A-B) #AB
N2 = np.linalg.norm(C-B) #BC
N3 = np.linalg.norm(D-C) #CD
N4 = np.linalg.norm(D-A) #DA
N5 = np.linalg.norm(Q-B) #BQ
N6 = np.linalg.norm(D-P) #DP

N11 = np.linalg.norm(A-P) #CD
N22 = np.linalg.norm(C-Q) #DA
N33 = np.linalg.norm(A-Q) #BQ
N44 = np.linalg.norm(C-P) #DP


#∠CBQ
angle1=((m_5)@(m_2))/(N5*N2)
a1=math.degrees (math.acos (angle1))
#∠ADP
angle2=((m_6)@(m_4))/(N4*N6)
a2=math.degrees (math.acos (angle2))

#∠ABQ
angle3=((m_1)@(m_5))/(N1*N5)
a3=math.degrees (math.acos (angle3))
#∠CDP
angle4=((m_3)@(m_6))/(N3*N6)
a4=math.degrees (math.acos (angle4))

#∠AQC
angle5=((n_2)@(n_3))/(N22*N33)
a5=math.degrees (math.acos (angle5))

#∠APC
angle6=((n_1)@(n_4))/(N11*N44)
a6=math.degrees (math.acos (angle6))

#∠PAQ
angle7=((n_1)@(n_3))/(N11*N33)
a7=math.degrees (math.acos (angle7))

#∠QCP
angle8=((n_2)@(n_4))/(N22*N44)
a8=math.degrees (math.acos (angle8))


if ((round(N5,4) == round(N6,4)) and (round(N2) == round(N4,4)) and (round(a1)==round(a2))):
	print("(i)∆ APD ≅ ∆ CQB")
   
if (round(N11,4) == round(N22,4)):
   print("(ii) AP=CQ")
   

if (round(N5,4) == round(N6,4)) and (round(N1,4) == round(N3,4)) and (a3==a4):
   print("(iii)∆ AQB ≅ ∆ CPD")
   
if (round(N33,4) == round(N44,4)):
   print("(iV) AQ=CP")
    
if (round(N11,4) == round(N22,4)) and (round(N33,4) == round(N44,4)) or ((a5==a6) and (a7==a8)):
   print(" (v) Quadrilateral APCQ is a parallelogram")
   

#Labeling the coordinates
tri_coords =np.vstack((B,C,D,A,Q,P)).T

plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['B','C','D','A','Q','P']
for i,txt in enumerate(vert_labels):
	plt.annotate(txt,
			(tri_coords[0,i],tri_coords[1,i]),
			textcoords="offset points",
			xytext=(0,10),
			ha='center')

plt.xlabel('$X$')
plt.ylabel('$Y$')
#plt.legend(loc='best')
plt.grid()
plt.axis('equal')


plt.savefig('/sdcard/FWCmodule1/Matrix_Lines/output.pdf')
subprocess.run(shlex.split("termux-open  /sdcard/FWCmodule1/Matrix_Lines/output.pdf"))

#plt.show()





