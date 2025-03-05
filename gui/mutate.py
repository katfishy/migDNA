import tkinter as tk

class Mutate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=mutate_text, justify="left").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=master.go_to_start).pack()


mutate_text = """
Paste your DNA sequence in the text box below and select the type of 
mutation. If you leave the location blank, a random location will be
chosen. If no mutation type is chosen, 
"""