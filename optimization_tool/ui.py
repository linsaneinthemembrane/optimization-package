import streamlit as st
from .optimizer import Optimizer
from .templates import generate_template, format_problem

class DisplayUI:
    def __init__(self):
        if "optimizer" not in st.session_state:
            st.session_state.optimizer = Optimizer()
            st.session_state.template = generate_template()
        self.optimizer = st.session_state.optimizer
        self.template = st.session_state.template

    def run(self):
        st.title("Optimization Problem Solver")
        self.display_objective()
        self.display_constraints()
        self.display_bounds()
        self.display_solution()

    def format_coefficient(self, c, i):
        if c == 1:
            return f"x_{{{i+1}}}"
        elif c == -1:
            return f"-x_{{{i+1}}}"
        else:
            return f"{c}x_{{{i+1}}}"

    def display_objective(self):
        st.subheader("Objective Function")
        obj_type = st.selectbox("Type", ["maximize", "minimize"], key="obj_type")
        
        if "num_vars" not in st.session_state:
            st.session_state.num_vars = len(self.template["objective_function"]["coefficients"])
        
        num_vars = st.number_input(
            "Number of Variables",
            min_value=1,
            value=st.session_state.num_vars,
            key="num_vars_input",
            step=1
        )
        
        if num_vars != st.session_state.num_vars:
            st.session_state.num_vars = num_vars
            self.update_template_for_new_vars(num_vars)
            st.experimental_rerun()
        
        new_coeffs = []
        for i in range(num_vars):
            coeff = st.number_input(
                f"Coefficient for x{i+1}",
                value=self.template["objective_function"]["coefficients"][i],
                key=f"obj_coeff_{i}",
                step=1
            )
            new_coeffs.append(coeff)
        
        self.template["objective_function"]["coefficients"] = new_coeffs
        self.optimizer.set_objective(new_coeffs, obj_type)
        
        objective_terms = [self.format_coefficient(c, i) for i, c in enumerate(new_coeffs)]
        objective_latex = f"{obj_type} \\space " + ' + '.join(objective_terms)
        st.latex(objective_latex)

    def update_template_for_new_vars(self, num_vars):
        while len(self.template["objective_function"]["coefficients"]) < num_vars:
            self.template["objective_function"]["coefficients"].append(1)
        while len(self.template["objective_function"]["coefficients"]) > num_vars:
            self.template["objective_function"]["coefficients"].pop()
        
        for constraint in self.template["constraints"]:
            while len(constraint["coefficients"]) < num_vars:
                constraint["coefficients"].append(0)
            while len(constraint["coefficients"]) > num_vars:
                constraint["coefficients"].pop()
        
        while len(self.template["bounds"]) < num_vars:
            self.template["bounds"].append((0, 100))
        while len(self.template["bounds"]) > num_vars:
            self.template["bounds"].pop()

    def display_constraints(self):
        st.subheader("Constraints")
        num_vars = len(self.template["objective_function"]["coefficients"])
        
        if st.button("Add Constraint"):
            new_constraint = {
                "coefficients": [0] * num_vars,
                "bound": 0,
                "type": "<="
            }
            self.template["constraints"].append(new_constraint)
            st.experimental_rerun()
        
        # Clear existing constraints in the optimizer
        self.optimizer.constraints = []
        
        for i, constraint in enumerate(self.template["constraints"]):
            st.markdown(f"**Constraint {i+1}**")
            cols = st.columns(num_vars + 2)
            new_coeffs = []
            
            for j in range(num_vars):
                with cols[j]:
                    coeff = st.number_input(
                        f"C{i+1} Coeff {j+1}",
                        value=constraint["coefficients"][j],
                        key=f"constraint_{i}_coeff_{j}",
                        step=1
                    )
                    new_coeffs.append(coeff)
            
            with cols[-2]:
                options = ["<=", "=", ">="]
                default_index = options.index(constraint["type"])
                constraint_type = st.selectbox(
                    "Type",
                    options=options,
                    index=default_index,
                    key=f"constraint_{i}_type"
                )
            
            with cols[-1]:
                bound = st.number_input(
                    "Bound",
                    value=constraint["bound"],
                    key=f"constraint_{i}_bound",
                    step=1
                )
            
            constraint["coefficients"] = new_coeffs
            constraint["type"] = constraint_type
            constraint["bound"] = bound
            
            # Add the constraint to the optimizer
            self.optimizer.add_constraint(new_coeffs, bound, constraint_type)
            
            constraint_terms = [self.format_coefficient(c, j) for j, c in enumerate(new_coeffs)]
            constraint_latex = ' + '.join(constraint_terms) + f" {constraint_type} {bound}"
            st.latex(constraint_latex)


    def display_bounds(self):
        st.subheader("Variable Bounds")
        num_vars = len(self.template["objective_function"]["coefficients"])
        self.optimizer.set_objective(
            self.template["objective_function"]["coefficients"],
            self.template["objective_function"]["type"]
        )
        
        new_bounds = []
        for i in range(num_vars):
            col1, col2 = st.columns(2)
            with col1:
                lower = st.number_input(
                    f"Lower bound for x{i+1}",
                    value=self.template["bounds"][i][0],
                    key=f"bound_lower_{i}",
                    step=1
                )
            with col2:
                upper = st.number_input(
                    f"Upper bound for x{i+1}",
                    value=self.template["bounds"][i][1],
                    key=f"bound_upper_{i}",
                    step=1
                )
            new_bounds.append((lower, upper))
            st.latex(f"{lower} \\leq x_{{{i+1}}} \\leq {upper}")
        
        self.template["bounds"] = new_bounds
        self.optimizer.set_bounds(new_bounds)

    def display_solution(self):
        if st.button("Solve", type="primary"):
            solution = self.optimizer.solve()
            st.write("Solution:", solution)  # Add this line for debugging
            if solution['success']:
                st.success("Optimal Solution Found!")
                for i, val in enumerate(solution['x']):
                    st.latex(f"x_{{{i+1}}} = {val:.4f}")
                st.latex(f"\\text{{Optimal Value: }} {solution['fun']:.4f}")
            else:
                st.error(f"Optimization Failed: {solution['message']}")
