import sympy as sp

# 1. Define Symbols
a, t, vi, vf, s = sp.symbols('a t vi vf s')

# 2. Define Kinematic Equations 
eq1 = sp.Eq(vf, vi + a * t)
eq2 = sp.Eq(s, vi * t + 0.5 * a * t**2)

print("--- Kinematic Calculator ---")

# 3. Get User Input
try:
    v_init = float(input("Enter initial velocity (m/s) [0 for standstill]: "))
    v_final_kmh = float(input("Enter target final velocity (km/h): "))
    time_val = float(input("Enter time duration (seconds): "))

    # convert km/h to m/s for the calculation
    v_final_ms = v_final_kmh / 3.6

    # 4. create data dictionary
    user_data = {vi: v_init, vf: v_final_ms, t: time_val}

    # 5. solve for Acceleration 
    sol_a = sp.solve(eq1.subs(user_data), a)
    accel_result = sol_a[0]

    # 6. solve for distance
    sol_s = sp.solve(eq2.subs(user_data).subs(a, accel_result), s)
    dist_result = sol_s[0]

    # 7. results
    print("\n- Results -")
    print(f"Required Acceleration: {accel_result:.2f} m/s²")
    print(f"Distance Traveled:     {dist_result:.2f} meters")

except ValueError:
    print("Invalid input! Please enter numerical values.")