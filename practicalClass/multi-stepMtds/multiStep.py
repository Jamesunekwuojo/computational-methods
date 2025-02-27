def adams_bashforth_2(y_n, y_n1, f_n, f_n1, h):
    return y_n1 + (h / 2) * (3 * f_n1 - f_n)

def adams_moulton_2(y_n1, f_n, f_n1, f_n2, h):
    return y_n1 + (h / 12) * (5 * f_n2 + 8 * f_n1 - f_n)

def adams_bashforth_3(y_n, y_n1, y_n2, f_n, f_n1, f_n2, h):
    return y_n2 + (h / 12) * (23 * f_n2 - 16 * f_n1 + 5 * f_n)

def adams_moulton_3(y_n2, y_n1, y_n, f_n, f_n1, f_n2, f_n3, h):
    return y_n2 + (h / 24) * (9 * f_n3 + 19 * f_n2 - 5 * f_n1 + f_n)

# Example usage
y_n, y_n1, y_n2 = 1.0, 1.1, 1.2  # Example initial values
f_n, f_n1, f_n2, f_n3 = 0.5, 0.6, 0.7, 0.8  # Example function values
h = 0.1  # Step size

# Compute next values
y_next_ab2 = adams_bashforth_2(y_n, y_n1, f_n, f_n1, h)
y_next_am2 = adams_moulton_2(y_n1, f_n, f_n1, f_n2, h)
y_next_ab3 = adams_bashforth_3(y_n, y_n1, y_n2, f_n, f_n1, f_n2, h)
y_next_am3 = adams_moulton_3(y_n2, y_n1, y_n, f_n, f_n1, f_n2, f_n3, h)

print("2-stage Adams Bashforth:", y_next_ab2)
print("2-stage Adams Moulton:", y_next_am2)
print("3-stage Adams Bashforth:", y_next_ab3)
print("3-stage Adams Moulton:", y_next_am3)
