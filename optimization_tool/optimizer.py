from scipy.optimize import linprog


class Optimizer:
    def __init__(self):
        """Initialize an Optimizer instance."""
        self.objective = None
        self.constraints = []
        self.bounds = []
        self.variables = []

    def set_objective(self, coefficients):
        """
        Define the objective function coefficients.
        Example:
            opt.set_objective([-3, -5])  # Maximize 3x1 + 5x2
        """
        self.objective = coefficients

    def add_constraint(self, coefficients, bound, constraint_type='<='):
        """
        Add a constraint.
        Example:
            opt.add_constraint([1, 2], 10, '<=')  # 1*x1 + 2*x2 <= 10
        """
        self.constraints.append((coefficients, bound, constraint_type))

    def set_bounds(self, bounds):
        """
        Set bounds for the decision variables.
        Example:
            opt.set_bounds([(0, None), (0, None)])  # x1, x2 >= 0
        """
        self.bounds = bounds

    def show_template(self):
        """
        Display a usage template for defining optimization problems.
        """
        template = """
        Example Usage:
        
        # Step 1: Create an Optimizer instance
        opt = Optimizer()
        
        # Step 2: Define the objective function
        opt.set_objective([c1, c2, ..., cn])  # Coefficients of the objective function
        
        # Step 3: Add constraints
        opt.add_constraint([a11, a12, ..., a1n], b1, '<=')  # Example constraint
        opt.add_constraint([a21, a22, ..., a2n], b2, '>=')  # Example constraint
        
        # Step 4: Define variable bounds
        opt.set_bounds([(0, None), (0, None)])  # Variable bounds
        
        # Step 5: Solve the problem
        result = opt.solve()
        print("Optimal Solution:", result.x)
        """
        print(template)

    def solve(self):
        """
        Solve the optimization problem using linear programming.
        """
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

        result = linprog(
            c=self.objective,
            A_ub=A_ub if A_ub else None,
            b_ub=b_ub if b_ub else None,
            A_eq=A_eq if A_eq else None,
            b_eq=b_eq if b_eq else None,
            bounds=self.bounds
        )
        return result
