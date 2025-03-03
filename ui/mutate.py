import tkinter as tk

class Mutate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=mutate_text, justify="left").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=self.go_to_start).pack()
    
    def go_to_start(self):
        from ui.start import StartPage
        self.master.switch_frame(StartPage)

mutate_text = """
Paste your DNA sequence in the text box below and select the type of 
mutation. If you leave the location blank, a random location will be
chosen. If no mutation type is chosen, 
"""