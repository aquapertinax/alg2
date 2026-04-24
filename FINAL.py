#i followed several tutorials to learn how to use customtkinter and sympy, as well as all of the kinematics used were taken from online.  Already had basic python knowdledge.



import customtkinter as ctk
import sympy as sp

# basic setup for the window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class f1_gui_sim(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("f1 overtake simulator v1.2")
        self.geometry("500x600")

        # define the algebraic symbols for the solver
        # item = time (x), buffer = distance (y)
        self.t, self.a, self.vi, self.vf, self.item, self.buffer = sp.symbols('t a vi vf item buffer')

        # ui elements
        self.label_title = ctk.CTkLabel(self, text="f1 overtake simulator", font=("arial", 24, "bold"))
        self.label_title.pack(pady=20)

        # input fields
        self.v_init = self.create_input("starting speed (m/s):", "0")
        self.v_final = self.create_input("target speed (km/h):", "320")
        self.t_target = self.create_input("time to target (s):", "4.5")
        self.rival_v = self.create_input("rival speed (m/s):", "75")
        self.rival_gap = self.create_input("rival head start (m):", "50")

        # run button
        self.btn_run = ctk.CTkButton(self, text="solve system", command=self.run_sim)
        self.btn_run.pack(pady=20)

        # output display
        self.output = ctk.CTkTextbox(self, height=150, width=450)
        self.output.pack(pady=10)

    def create_input(self, label_text, placeholder):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, fill="x", padx=50)
        lbl = ctk.CTkLabel(frame, text=label_text, width=150, anchor="w")
        lbl.pack(side="left")
        ent = ctk.CTkEntry(frame)
        ent.insert(0, placeholder)
        ent.pack(side="right", expand=True, fill="x")
        return ent

    def run_sim(self):
        try:
            # step 1: pull values from the gui
            vi_val = float(self.v_init.get())
            vf_val_ms = float(self.v_final.get()) / 3.6 # unit conversion
            t_val = float(self.t_target.get())
            rv_val = float(self.rival_v.get())
            rg_val = float(self.rival_gap.get())

            # step 2: calculate car acceleration
            # a = (vf - vi) / t -> finding the slope of the velocity curve
            accel_expr = (self.vf - self.vi) / self.t
            accel_val = accel_expr.subs({self.vi: vi_val, self.vf: vf_val_ms, self.t: t_val})

            # step 3: calculate distance to reach top speed
            # d = vi*t + 0.5*a*t^2 -> calculating area under the curve
            dist_expr = self.vi * self.t + 0.5 * self.a * self.t**2
            dist_val = dist_expr.subs({self.vi: vi_val, self.t: t_val, self.a: accel_val})

            # step 4: build the system of equations for the constant speed phase
            # eq1: y = mx (player car line)
            eq_player = sp.Eq(self.buffer, vf_val_ms * self.item)
            # eq2: y = mx + b (rival car line with y-intercept)
            eq_rival = sp.Eq(self.buffer, rv_val * self.item + rg_val)

            # step 5: solve for the intersection point (item/time, buffer/distance)
            sol = sp.solve((eq_player, eq_rival), (self.item, self.buffer))

            if not sol or sol[self.item] <= 0:
                res = "result: no overtake possible.\nthe lines are diverging or parallel."
            else:
                t_res = float(sol[self.item])
                d_res = float(sol[self.buffer])
                
                res = f"overtake confirmed!\n"
                res += f"------------------------\n"
                res += f"accel: {float(accel_val):.2f} m/s²\n"
                res += f"dist to reach top speed: {float(dist_val):.2f}m\n"
                res += f"time to catch (x): {t_res:.2f}s\n"
                res += f"total distance (y): {d_res:.2f}m"

            self.output.delete("1.0", "end")
            self.output.insert("1.0", res)

        except Exception as e:
            self.output.delete("1.0", "end")
            self.output.insert("1.0", f"error: {e}")

if __name__ == "__main__":
    app = f1_gui_sim()
    app.mainloop()
