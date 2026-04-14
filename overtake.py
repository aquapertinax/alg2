
import sympy as sp

x, y = sp.symbols('x y')


# System:
# 2x + y = 10
#  x - y = 2
eq1 = sp.Eq(2*x + y, 10)
eq2 = sp.Eq(x - y, 2)


# solve for x and y
solution = sp.solve((eq1, eq2), (x, y), dict=True)

print(solution) 
# Output: [{x: 4, y: 2}]


import sympy as sp

def solve_system():
    x, y = sp.symbols('x y')
    
    print("Enter the coefficients for ax + by = c")
    a1 = float(input("Eq1 a: "))
    b1 = float(input("Eq1 b: "))
    c1 = float(input("Eq1 c: "))
    
    a2 = float(input("Eq2 a: "))
    b2 = float(input("Eq2 b: "))
    c2 = float(input("Eq2 c: "))

    eq1 = sp.Eq(a1*x + b1*y, c1)
    eq2 = sp.Eq(a2*x + b2*y, c2)

    result = sp.solve((eq1, eq2), (x, y))
    print(f"Solution: {result}")

solve_system()
             


