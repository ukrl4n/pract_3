import numpy as np
from scipy.optimize import curve_fit

# Дані
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([0.1, 3, 8.1, 14.9, 23.9])

x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([2.9, 6.1, 9.2, 11.8, 16])

# 1. Лінійне рівняння: y = ax + b
def linear_model(x, a, b):
    return a * x + b

params_linear, _ = curve_fit(linear_model, x1, y1)
a1, b1 = params_linear

# 2. Квадратичне рівняння: y = ax^2 + b
def quadratic_model(x, a, b):
    return a * x**2 + b

params_quadratic, _ = curve_fit(quadratic_model, x2, y2)
a2, b2 = params_quadratic

# 3. Кубічне рівняння: y = ax^3 + bx^2 + c
def cubic_model(x, a, b, c):
    return a * x**3 + b * x**2 + c

params_cubic, _ = curve_fit(cubic_model, x2, y2)
a3, b3, c3 = params_cubic

# 4. Тригонометричне рівняння: y = a * cos(2x) + b * sin(x)
def trig_model(x, a, b):
    return a * np.cos(2*x) + b * np.sin(x)

params_trig, _ = curve_fit(trig_model, x2, y2)
a4, b4 = params_trig

# Вивід результатів
print("Лінійне рівняння: y = ax + b")
print(f"a = {a1}, b = {b1}")

print("\nКвадратичне рівняння: y = ax^2 + b")
print(f"a = {a2}, b = {b2}")

print("\nКубічне рівняння: y = ax^3 + bx^2 + c")
print(f"a = {a3}, b = {b3}, c = {c3}")

print("\nТригонометричне рівняння: y = a*cos(2x) + b*sin(x)")
print(f"a = {a4}, b = {b4}")
