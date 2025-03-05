import tkinter as tk

class Identify(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=identify_text).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=master.go_to_start).pack()
        
identify_text = """
Paste 2 DNA sequences to identify whether 
there is a single nucleotide mutation.
"""