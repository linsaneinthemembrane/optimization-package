from scipy.optimize import linprog
import numpy as np

class Optimizer:
    def __init__(self):
        self.objective = None
        self.constraints = []
        self.bounds = []
        self.variables = []
    
    def set_objective(self, coefficients):
        """Define the objective function coefficients."""
        self.objective = coefficients
    
    def add_constraint(self, coefficients, bound, constraint_type='<='):
        """Add a constraint: coefficients @ variables [<=, >=, =] bound."""
        self.constraints.append((coefficients, bound, constraint_type))
    
    def set_bounds(self, bounds):
        """Set bounds for the decision variables."""
        self.bounds = bounds

    def solve(self):
        """Solve the optimization problem using linear programming."""
        A, b, constraint_types = [], [], []
        for coeff, bound, ctype in self.constraints:
            A.append(coeff)
            b.append(bound)
            constraint_types.append(ctype)
        
        A_eq, b_eq, A_ub, b_ub = [], [], [], []
        for i, ctype in enumerate(constraint_types):
            if ctype == '=':
                A_eq.append(A[i])
                b_eq.append(b[i])
            elif ctype == '<=':
                A_ub.append(A[i])
                b_ub.append(b[i])
            elif ctype == '>=':
                A_ub.append([-x for x in A[i]])
                b_ub.append(-b[i])

        result = linprog(c=self.objective, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=self.bounds)
        return result
