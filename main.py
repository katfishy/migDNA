from mutations import *
import tkinter as tk

class MutationSim(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=instruction_text, justify="left").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Mutate",
                  command=lambda: master.switch_frame(Mutate)).pack()
        tk.Button(self, text="Identify",
                  command=lambda: master.switch_frame(Identify)).pack()
        tk.Button(self, text="Generate",
                command=lambda: master.switch_frame(Generate)).pack()
        

# button_mutate = tk.Button(frm_buttons, text="Mutate", command=open_mutate_window)
# button_identify = tk.Button(frm_buttons, text="Identify")
# button_random = tk.Button(frm_buttons, text="Random")

# button_mutate.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# button_identify.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
# button_random.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


class Mutate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=mutate_text, justify="left").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class Identify(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=identify_text).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class Generate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=generate_text).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


instruction_text = """
Welcome to DNA Mutation Simulator.

Mutate: Add a single nucleotide mutation to a DNA sequence.
Identify: Identify the single nucleotide mutation in 2 DNA sequences.
Generate: Generate a random DNA sequence of desired length.
"""

mutate_text = """
Paste your DNA sequence in the text box below and select the type of 
mutation. If you leave the location blank, a random location will be
chosen. If no mutation type is chosen, 
"""

identify_text = """
Paste 2 DNA sequences to identify whether 
there is a single nucleotide mutation.
"""

generate_text = """
Generate a random DNA sequence of desired length.
"""

if __name__ == "__main__":
    app = MutationSim()
    app.mainloop()