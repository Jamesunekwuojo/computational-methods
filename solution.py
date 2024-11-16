import numpy as np
import sympy as sp

# Define the recurrence relation
def solve_difference_equation(n_terms=10):
    # Coefficients of the homogeneous equation
    a2, a1, a0 = 1, -1, 5/2

    # Solve the characteristic equation: r^2 - r + 5/2 = 0
    r = sp.symbols('r')
    char_eq = a2 * r**2 + a1 * r + a0
    roots = sp.solve(char_eq, r)

    # Display roots
    print(f"Roots of the characteristic equation: {roots}")

    # Particular solution for the non-homogeneous part
    n = sp.symbols('n')
    particular_sol = sp.Function('p')(n)
    rhs = 5 * sp.sin(sp.pi * n / 4)

    # Assume a particular solution of the form: Asin(nπ/4) + Bcos(nπ/4)
    A, B = sp.symbols('A B')
    particular_sol_guess = A * sp.sin(sp.pi * n / 4) + B * sp.cos(sp.pi * n / 4)

    # Substitute guess into the original equation and solve for A and B
    eq = (
        particular_sol_guess.subs(n, n + 2)
        - particular_sol_guess.subs(n, n + 1)
        + (5 / 2) * particular_sol_guess
        - rhs
    )
    A_B_solution = sp.solve([sp.expand(eq.coeff(sp.sin(sp.pi * n / 4))), sp.expand(eq.coeff(sp.cos(sp.pi * n / 4)))], (A, B))

    print(f"Particular solution coefficients: {A_B_solution}")

    # Combine homogeneous and particular solutions
    C1, C2 = sp.symbols('C1 C2')
    general_sol = (
        C1 * roots[0]**n + C2 * roots[1]**n + A_B_solution[A] * sp.sin(sp.pi * n / 4) + A_B_solution[B] * sp.cos(sp.pi * n / 4)
    )
    print(f"General solution: {general_sol}")

    # Generate terms of the sequence
    terms = []
    for i in range(n_terms):
        terms.append(general_sol.subs({n: i, C1: 1, C2: 1}).evalf())  # Assuming initial conditions C1 = C2 = 1
    return terms


# Solve and print the solution
n_terms = 10  # Number of terms to generate
sequence = solve_difference_equation(n_terms=n_terms)
print(f"First {n_terms} terms of the sequence: {sequence}")
