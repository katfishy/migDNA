import tkinter as tk

class Identify(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=identify_text).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=self.go_to_start).pack()
        
    def go_to_start(self):
        from ui.start import StartPage
        self.master.switch_frame(StartPage)

identify_text = """
Paste 2 DNA sequences to identify whether 
there is a single nucleotide mutation.
"""