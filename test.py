from optimization_tool.optimizer import Optimizer
from optimization_tool.templates import generate_template
from optimization_tool.ui import display_latex_with_tooltip

# Example Problem
opt = Optimizer()
opt.set_objective([-3, -5])  # Coefficients for the objective function
opt.add_constraint([1, 0], 4, '<=')
opt.add_constraint([0, 2], 12, '<=')
opt.add_constraint([3, 2], 18, '<=')
opt.set_bounds([(0, None), (0, None)])  # Bounds for decision variables

result = opt.solve()
print("Optimal Solution:", result.x)

# Display Template
template = generate_template()
print("Template:", template)
