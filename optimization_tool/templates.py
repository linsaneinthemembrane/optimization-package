def generate_template(num_variables=2):
    """Generate default template for Streamlit."""
    template = {
        "objective_function": {
            "type": "maximize",
            "coefficients": [1] * num_variables
        },
        "constraints": [
            {
                "coefficients": [1] * num_variables,
                "bound": 10,
                "type": "<="
            }
        ],
        "bounds": [(0, 100)] * num_variables
    }
    return template

def format_problem(template):
    """Using LaTeX formatting."""
    obj_type = template["objective_function"]["type"]
    obj_coeffs = template["objective_function"]["coefficients"]
    
    # Format objective function
    obj_terms = [f"{c if c != 1 else ''}x_{{{i+1}}}" for i, c in enumerate(obj_coeffs)]
    obj_str = f"{obj_type} \\space {' + '.join(obj_terms)}"
    
    # Format constraints
    constraints = []
    for constraint in template["constraints"]:
        coeffs = constraint["coefficients"]
        bound = constraint["bound"]
        ctype = constraint["type"]
        terms = [f"{c if c != 1 else ''}x_{{{i+1}}}" for i, c in enumerate(coeffs)]
        constraints.append(f"{' + '.join(terms)} {ctype} {bound}")
    
    # Format bounds
    bounds = [f"{l} \\leq x_{{{i+1}}} \\leq {u}" for i, (l, u) in enumerate(template["bounds"])]
    
    return {
        "objective": obj_str,
        "constraints": constraints,
        "bounds": bounds
    }
