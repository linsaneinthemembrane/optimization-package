# Linear Programming Optimization Tool


![2025-01-14 21-46-39](https://github.com/user-attachments/assets/ff06ffbe-618d-4844-b71c-a430dd9bd5f2)


An interactive web application for solving linear programming problems using the Simplex method. Built with Streamlit and Python, this tool provides a user-friendly interface for defining and solving optimization problems. 

Originally, this project started with trying to create my own optimization problem-solving algorithm but pivoted to focus on building a user interface for existing solvers. This pivot allowed for a deeper exploration of front-end development and application architecture.

## Features

- Interactive UI for defining optimization problems
- Support for both maximization and minimization problems
- Dynamic variable and constraint management (-/+)
- Variable bounds configuration
- Real-time LaTeX rendering of mathematical expressions
- Utilizes HiGHS solver for optimization

## Learning Outcomes

### Streamlit Development
- Built interactive web apps with Streamlit's component system
- Managed application state using `st.session_state`
- Created dynamic UI elements with real-time updates
- Implemented form validation and error handling

### Frontend Design
- Rendered mathematical expressions using LaTeX in Streamlit
- Designed responsive layouts with column systems
- Created intuitive interfaces for complex mathematical input
- Developed real-time result visualization

### Architecture Skills
- Structured modular Python applications[1]
- Separated concerns between UI, business logic, and computation
- Integrated third-party optimization solvers
- Managed state across multiple components


## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/optimizer-tool.git
cd optimizer-tool
```
2. Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```
3. Install required packages:
```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```
streamlit run app.py
```

2. In the web interface:
   - Select optimization type (maximize/minimize)
   - Set number of variables
   - Define objective function coefficients
   - Add constraints with coefficients and bounds
   - Set variable bounds
   - Click "Solve" to obtain the solution

## Next Steps

1. Implement custom Simplex solver to replace current implementation
2. Add support for:
   - Integer programming
   - Problem visualization
   - Solution sensitivity analysis
4. Implement solution visualization
5. Add problem validation and error checking

## Dependencies

- Streamlit
- NumPy
- SciPy
- SymPy (for LaTeX rendering)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
