import numpy as np
from scipy.optimize import linprog

def simplex_solver(objective_coeffs, optimization_type="minimize", constraints=None, bounds=None):
    # Convert to numpy array
    c = np.array(objective_coeffs, dtype=float)
    
    # Negate for maximization
    if optimization_type == 'maximize':
        c = -c
    
    # Process constraints
    A_ub = []
    b_ub = []
    A_eq = []
    b_eq = []
    
    if constraints:
        for coeffs, bound, ctype in constraints:
            coeffs_array = np.array(coeffs, dtype=float)
            bound_val = float(bound)
            
            if ctype == '>=':
                A_ub.append(-coeffs_array)
                b_ub.append(-bound_val)
            elif ctype == '<=':
                A_ub.append(coeffs_array)
                b_ub.append(bound_val)
            elif ctype == '=':
                A_eq.append(coeffs_array)
                b_eq.append(bound_val)
    
    # Convert to numpy arrays
    A_ub = np.array(A_ub) if A_ub else None
    b_ub = np.array(b_ub) if b_ub else None
    A_eq = np.array(A_eq) if A_eq else None
    b_eq = np.array(b_eq) if b_eq else None
    
    result = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method='highs'
    )
    
    # Adjust the objective value for maximization problems
    fun = -result.fun if optimization_type == 'maximize' else result.fun
    
    return {
        'success': result.success,
        'x': result.x,
        'fun': fun,  
        'message': result.message
    }

# Add alias for backward compatibility
custom_solver = simplex_solver
