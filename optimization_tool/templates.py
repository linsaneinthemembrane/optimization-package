def generate_template():
    template = {
        "objective_function": "maximize/minimize c1*x1 + c2*x2 + ... + cn*xn",
        "constraints": [
            "a11*x1 + a12*x2 + ... + a1n*xn <= b1",
            "a21*x1 + a22*x2 + ... + a2n*xn = b2"
        ],
        "variables": "x1, x2, ..., xn >= 0"
    }
    return template
