import numpy as np
from .solver import custom_solver

class Optimizer:
    def __init__(self):
        self.objective = None
        self.constraints = []
        self.bounds = []
        self.variables = []
        self.optimization_type = "maximize"

    def set_objective(self, coefficients, optimization_type="maximize"):
        """Set objective function coefficients and optimization type."""
        self.objective = [float(c) for c in coefficients]
        self.optimization_type = optimization_type
        self.variables = [f"x{i+1}" for i in range(len(coefficients))]

    def add_constraint(self, coefficients, bound, constraint_type='<='):
        """Add a constraint button to the optimization problem."""
        # all inputs -> float to avoid integer division issues
        coefficients = [float(c) for c in coefficients]
        bound = float(bound)
        self.constraints.append((coefficients, bound, constraint_type))

    def remove_constraint(self, index):
        """Remove a constraint starting from the last."""
        if 0 <= index < len(self.constraints):
            del self.constraints[index]
        else:
            raise IndexError("Constraint index out of range")

    def set_bounds(self, bounds):
        """Set variable bounds."""
        if len(bounds) != len(self.variables):
            raise ValueError("Number of bounds must match number of variables")
        self.bounds = [(float(lower), float(upper)) for lower, upper in bounds] if bounds else None

    def solve(self):
        """Solve the optimization problem using custom_solver."""
        # Ensure all components are properly set
        if self.objective is None:
            return {
                'success': False,
                'message': 'Objective function not set'
            }

        # Convert constraints to the format expected by custom_solver
        formatted_constraints = []
        for coeffs, bound, ctype in self.constraints:
            formatted_constraints.append((coeffs, bound, ctype))

        result = custom_solver(
            objective_coeffs=self.objective,
            optimization_type=self.optimization_type,
            constraints=formatted_constraints,
            bounds=self.bounds
        )

        return result

    def get_problem_summary(self):
        """Returns summary of problem values."""
        return {
            "objective": self.objective,
            "optimization_type": self.optimization_type,
            "variables": self.variables,
            "constraints": self.constraints,
            "bounds": self.bounds
        }
