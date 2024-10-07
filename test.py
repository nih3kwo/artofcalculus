from pycosat import Solver

# Define the rules as clauses
clauses = [
    [1, 2], # Rule (a): p1 AND p2
    [-1, -2], # Rule (b): (NOT p1) OR (NOT p2)
]

# Create a SAT solver
solver = Solver()

# Add the clauses to the solver
for clause in clauses:
    solver.add_clause(clause)

# Check for satisfiability
status = solver.solve()

# Get the model
if status == 1:
    model = solver.get_model()
    print("Satisfiable! Model:", model)
else:
    print("Unsatisfiable!")

# Interpretation of the model
if model:
    winning_coalition = [i + 1 for i, val in enumerate(model) if val == 1]
    print("Winning coalition:", winning_coalition)