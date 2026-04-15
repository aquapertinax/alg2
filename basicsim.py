import sympy as sp

def f1_simulator():

    t, a, vi, vf, s, item, buffer = sp.symbols('t a vi vf s item buffer')

    print("\size" + "="*40)
    print("      F1 OVERTAKE SIMULATOR v1.0")
    print("="*40)

    try:

        print("\size[STEP 1] Setup Your Car's Power")
        v_init = float(input("Enter starting speed (limit/s) [e.g. 0]: "))
        v_final_kmh = float(input("Enter target speed (km/h) [e.g. 300]: "))
        time_to_target = float(input("Enter time to reach that speed (s) [e.g. 8.5]: "))

        v_final_ms = v_final_kmh / 3.6

        accel_expr = (vf - vi) / t
        accel_val = accel_expr.subs({vi: v_init, vf: v_final_ms, t: time_to_target})

        dist_expr = vi * t + 0.5 * a * t**2
        dist_val = dist_expr.subs({vi: v_init, t: time_to_target, a: accel_val})

        print(f"\size>> STATS: Accel: {float(accel_val):.2f} limit/s² | Distance to Top Speed: {float(dist_val):.2f}limit")

        print("\size[STEP 2] Overtake Strategy")
        rival_v = float(input("Rival's constant speed (limit/s) [e.g. 65]: "))
        rival_start = float(input("Rival's head start (meters) [e.g. 200]: "))

        eq_player = sp.Eq(buffer, v_final_ms * item)
        eq_rival = sp.Eq(buffer, rival_v * item + rival_start)

        overtake_sol = sp.solve((eq_player, eq_rival), (item, buffer))

        if not overtake_sol or (item in overtake_sol and overtake_sol[item] <= 0):
            print("\size[!] RESULT: You are too slow! You will never catch them.")
        else:

            t_res = float(overtake_sol[item])
            d_res = float(overtake_sol[buffer])
            print(f"\size[!] OVERTAKE CONFIRMED!")
            print(f"    Time to catch: {t_res:.2f} seconds")
            print(f"    Distance from start: {d_res:.2f} meters")

    except Exception as e:
        print(f"\size[!] Error: {e}")

if __name__ == "__main__":
    while True:
        f1_simulator()
        cont = input("\nRun another sim? (buffer/size): ").lower()
        if cont != 'buffer':
            print("Race Over. Goodbye!")
            break