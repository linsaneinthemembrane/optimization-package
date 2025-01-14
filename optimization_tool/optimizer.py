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
        self.objective = coefficients
        self.optimization_type = optimization_type
        self.variables = [f"x{i+1}" for i in range(len(coefficients))]

    def add_constraint(self, coefficients, bound, constraint_type='<='):
        if len(coefficients) != len(self.variables):
            raise ValueError("Number of coefficients must match number of variables")
        self.constraints.append((coefficients, bound, constraint_type))

    def remove_constraint(self, index):
        if 0 <= index < len(self.constraints):
            del self.constraints[index]
        else:
            raise IndexError("Constraint index out of range")

    def set_bounds(self, bounds):
        if len(bounds) != len(self.variables):
            raise ValueError("Number of bounds must match number of variables")
        self.bounds = bounds

    def solve(self):
        """
        Solve the optimization problem using custom solver.
        """
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
        return {
            "objective": self.objective,
            "optimization_type": self.optimization_type,
            "variables": self.variables,
            "constraints": self.constraints,
            "bounds": self.bounds
        }
