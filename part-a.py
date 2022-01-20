import cplex

model = cplex.Cplex()  # creating the model object

objective = [0.28, 0.25, 0.17, 0.40]  # coefficients of the objective function


lower_bounds = [20, 20, 10, 20]  # no need to specify lines 7,8, and 9 as they are at default values

upper_bounds = [80, 100, 100, 50]

variable_names = ['X1', 'X3', 'X4', 'X7']

variable_types = ['C', 'C', 'C', 'C']  # 'C' for continuous!

# These were not passed to the add() function as specifying any
# of the types for decision variables makes the problem into a MIP
# which is not needed for this simple LP...
model.variables.add(obj = objective,
                     lb = lower_bounds,
                     ub = upper_bounds,
                     names = variable_names,
                     types= variable_types)# or equivalently types = "CIB")

# It is a maximization problem
model.objective.set_sense(model.objective.sense.maximize)

# Now we get ready to add the constraints
constraint_names = ['first']
first_constraint = [['X1', 'X3', 'X4', 'X7'], [1.0, 1.0, 1.0, 1.0]]

# model.add(model.if_then('X1' >= 20, 'Y1' == 1))

constraints = [first_constraint]
rhs = [100]

constraint_senses = ['E']
model.linear_constraints.add(lin_expr=constraints,
                             senses=constraint_senses,
                             rhs=rhs,
                             names=constraint_names)

model.solve()

pValue =-5*1 - 0.5*1 - 12*0 - 8*0 - 5*1 - 5*1  - 1*0 - 3*0 - 2*0
y_value = -5*1 - 6*0  - 4*1 - 4*1 - 8*0 - 6*0 - 7*1

toDeduct = y_value + pValue # a constant from the equation as p values and all are constant
print("Obj Value:", model.solution.get_objective_value() + toDeduct)
print("Values of Decision Variables:", model.solution.get_values())
model.solution.write('LP_solution.txt')  # creates a new file and stores the attr.
# of the solution in a written format
