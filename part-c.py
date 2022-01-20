#!/usr/bin/env python
# coding: utf-8

# In[7]:


import gurobipy as gp
from gurobipy import *

# vector of features
p = [1,1,0,0,1,1,0,0,0]

# Q threshold
Q = 25

lower_bound = [20,10,20,10,10,20,20]
upper_bound = [80,50,100,100,70,90,50]

# base regimen 
y_base_i = [1, 0, 1, 1, 0, 0, 1]
x_base_i = [20, 0, 30, 15, 0, 0, 35]

# costs
fc_i = [25, 50, 10, 25, 20, 30, 40]
uc_i = [1, 2, 1, 3, 2, 1, 1]

m = gp.Model()
    
# add x decision variable
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2")
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3")
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4")
x5 = m.addVar(vtype=GRB.CONTINUOUS, name="x5")
x6 = m.addVar(vtype=GRB.CONTINUOUS, name="x6")
x7 = m.addVar(vtype=GRB.CONTINUOUS, name="x7")

x = [x1, x2, x3, x4, x5, x6, x7]

# add y decision variable
y1 = m.addVar(vtype=GRB.BINARY, name="y1")
y2 = m.addVar(vtype=GRB.BINARY, name="y2")
y3 = m.addVar(vtype=GRB.BINARY, name="y3")
y4 = m.addVar(vtype=GRB.BINARY, name="y4")
y5 = m.addVar(vtype=GRB.BINARY, name="y5")
y6 = m.addVar(vtype=GRB.BINARY, name="y6")
y7 = m.addVar(vtype=GRB.BINARY, name="y7")

y = [y1, y2, y3, y4, y5, y6, y7]

# add c decision variable 
c1 = m.addVar(vtype=GRB.CONTINUOUS, name="c1")
c2 = m.addVar(vtype=GRB.CONTINUOUS, name="c2")
c3 = m.addVar(vtype=GRB.CONTINUOUS, name="c3")
c4 = m.addVar(vtype=GRB.CONTINUOUS, name="c4")
c5 = m.addVar(vtype=GRB.CONTINUOUS, name="c5")
c6 = m.addVar(vtype=GRB.CONTINUOUS, name="c6")
c7 = m.addVar(vtype=GRB.CONTINUOUS, name="c7")

c = [c1, c2, c3, c4, c5, c6, c7]

# add abs value decision variable
a1 = m.addVar(vtype=GRB.BINARY, name="a1")
a2 = m.addVar(vtype=GRB.BINARY, name="a2")
a3 = m.addVar(vtype=GRB.BINARY, name="a3")
a4 = m.addVar(vtype=GRB.BINARY, name="a4")
a5 = m.addVar(vtype=GRB.BINARY, name="a5")
a6 = m.addVar(vtype=GRB.BINARY, name="a6")
a7 = m.addVar(vtype=GRB.BINARY, name="a7")

a = [a1, a2, a3, a4, a5, a6, a7]

# add add decision variable
add1 = m.addVar(vtype=GRB.BINARY, name="add1")
add2 = m.addVar(vtype=GRB.BINARY, name="add2")
add3 = m.addVar(vtype=GRB.BINARY, name="add3")
add4 = m.addVar(vtype=GRB.BINARY, name="add4")
add5 = m.addVar(vtype=GRB.BINARY, name="add5")
add6 = m.addVar(vtype=GRB.BINARY, name="add6")
add7 = m.addVar(vtype=GRB.BINARY, name="add7")

add = [add1, add2, add3, add4, add5, add6, add7]

# add remove decision variable
remove1 = m.addVar(vtype=GRB.BINARY, name="remove1")
remove2 = m.addVar(vtype=GRB.BINARY, name="remove2")
remove3 = m.addVar(vtype=GRB.BINARY, name="remove3")
remove4 = m.addVar(vtype=GRB.BINARY, name="remove4")
remove5 = m.addVar(vtype=GRB.BINARY, name="remove5")
remove6 = m.addVar(vtype=GRB.BINARY, name="remove6")
remove7 = m.addVar(vtype=GRB.BINARY, name="remove7")

remove = [remove1, remove2, remove3, remove4, remove5, remove6, remove7]

# add w variable 
w = m.addVar(vtype=GRB.BINARY, name="w")

M = 1000

# objective function
m.setObjective(quicksum(fc_i[i]*c[i] + uc_i[i]*a[i] for i in range(0, 7)), GRB.MINIMIZE)

# quality of life equation constraint
p_value = -5*1 -0.5*1 -12*0 -8*0 -5*1 -5*1 -1*0 -3*0 -2*0
x_value = 0.28*x[0] + 0.3*x[1] + 0.25*x[2] + 0.17*x[3] + 0.31*x[4] + 0.246*x[5] + 0.4*x[6]
y_value = -5*y[0] - 6*y[1] - 4*y[2] - 4*y[3] - 8*y[4] - 6*y[5] - 7*y[6]
q_constraint_value = p_value + x_value + y_value
m.addConstr(q_constraint_value, GRB.EQUAL, Q)

# c constraints
m.addConstr(c[0] == 1 - y[0],)
m.addConstr(c[1] == y[1])
m.addConstr(c[2] == 1 - y[2])
m.addConstr(c[3] == 1 - y[3])
m.addConstr(c[4] == y[4])
m.addConstr(c[5] == y[5])
m.addConstr(c[6] == 1 - y[6])
m.update()

# abs value of add and remove constraint
m.addConstr(add[0] + remove[0] <= 1)
m.addConstr(add[1] + remove[1] <= 1)
m.addConstr(add[2] + remove[2] <= 1)
m.addConstr(add[3] + remove[3] <= 1)
m.addConstr(add[4] + remove[4] <= 1)
m.addConstr(add[5] + remove[5] <= 1)
m.addConstr(add[6] + remove[6] <= 1)
m.update()
    
# lower bound and upper bound of x constraint    
for i in range(0, 7):
    m.addConstr(x[i] >= lower_bound[i] * y[i])
    m.addConstr(x[i] <= upper_bound[i] * y[i])
    m.update()

# equal to 100 constraint - 200 due to infeasibility    
m.addConstr(quicksum(x[i] for i in range(0, 7)), GRB.EQUAL, 200)

# new constraints
m.addConstr(x[0] + x[1] >= 50*y[0]*y[1])
m.addConstr(x[0] + x[1] <= 70*y[0]*y[1] + M*(1-y[0]*y[1]))
m.addConstr((1 - y[4])*x[2] <= 25)
m.addConstr(w, GRB.EQUAL, y[3]*y[5])
m.addConstr(w * (y[4] + y[6] - 1) >= 0)

m.optimize()
m.printAttr('X')
m.update()


# In[ ]:




