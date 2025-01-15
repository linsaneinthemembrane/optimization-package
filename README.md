# Linear Programming Optimization Tool

An interactive web application for solving linear programming problems using the Simplex method. Built with Streamlit and Python, this tool provides a user-friendly interface for defining and solving optimization problems.

## Features

- Interactive UI for defining optimization problems
- Support for both maximization and minimization problems
- Dynamic variable management (add/remove variables)
- Constraint management system (add/remove constraints)
- Variable bounds configuration
- Real-time LaTeX rendering of mathematical expressions
- Utilizes HiGHS solver for optimization

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

## License

This project is licensed under the MIT License - see the LICENSE file for details.
