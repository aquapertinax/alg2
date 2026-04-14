import sympy as sp


# a = acceleration, t = time, vi = initial velocity, vf = final velocity, s = distance
a, t, vi, vf, s = sp.symbols('a t vi vf s')

# 2. kinematic Equations 
eq1 = sp.Eq(vf, vi + a * t)
eq2 = sp.Eq(s, vi * t + 0.5 * a * t**2)

# Solve for Acceleration 
# acceleration needed to reach 100 km/h (27.7 m/s) in 2.6 seconds

f1_data = {vi: 0, vf: 27.7, t: 2.6}
sol_a = sp.solve(eq1.subs(f1_data), a)

print(f"Required Acceleration: {sol_a[0]:.2f} m/s²")

# Find distance covered 
dist_covered = sp.solve(eq2.subs(f1_data).subs(a, sol_a[0]), s)
print(f"Distance traveled in 2.6s: {dist_covered[0]:.2f} meters")


