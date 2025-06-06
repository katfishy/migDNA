import tkinter as tk
from mutations import *

class Mutate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(
        self,
        bg = "#FFFFFF",
        height = 500,
        width = 500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
        
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_text(
            18.0,
            17.0,
            anchor="nw",
            text="Mutate",
            fill="#0B2F59",
            font=("Inter", 48 * -1, 'bold')
        )

        master.button_images = {
        "homebutton": tk.PhotoImage(file="./assets/home_button.png"),
        "homebutton_hover": tk.PhotoImage(file="./assets/home_button.png"),
        "generate": tk.PhotoImage(file="./assets/generate_button.png"),
        "generate_hover": tk.PhotoImage(file="./assets/generate_button.png"),
        }

        mutation_options = [
            "Insertion",
            "Deletion",
            "Substitution"
        ]

        master.create_button(self, "homebutton", 60, 60, 422, 21, master.go_to_start)
        master.create_button(self, "generate", 464, 65, 18, 201, self.mutate_sequence)


        self.mut_clicked = tk.StringVar()
        self.mut_clicked.set("Select Mutation Type")

        mutation_drop = tk.OptionMenu(self.canvas, self.mut_clicked, *mutation_options)
        mutation_drop.pack()

        self.nuc_clicked = tk.StringVar()
        self.nuc_clicked.set("Select Nucleotide")

        nucleotide_drop = tk.OptionMenu(self.canvas, self.nuc_clicked, *Nucleotides)
        nucleotide_drop.pack()

        self.sequence_input = tk.StringVar()
        self.sequence_entry = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=3,
            textvariable=self.sequence_input,
            font=("Inter", 16 * -1),
            relief="solid",
            highlightcolor="#1172E3",
            highlightbackground="#1172E3"
        )
        self.sequence_entry.place(
            x=18.0,
            y=193.0,
            width=464.0,
            height=43.0
        )

        self.position_input = tk.StringVar()
        self.position_entry = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=3,
            textvariable=self.position_input,
            font=("Inter", 16 * -1),
            relief="solid",
            highlightcolor="#1172E3",
            highlightbackground="#1172E3"
        )
        self.position_entry.place(
            x=18.0,
            y=155.0,
            width=43.0,
            height=43.0
        )

        self.new_sequence_box = tk.Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=3,
            font=("Inter", 16 * -1),
            relief="solid",
            highlightcolor="#1172E3",
            highlightbackground="#1172E3"
        )
        self.new_sequence_box.place(
            x=18.0,
            y=280.0,
            width=464.0,
            height=197.0
        )
    
    def mutate_sequence(self):
        """Mutates the given sequence based on user selection
        for mutation type."""
        mut_type = self.mut_clicked.get()
        sequence = self.sequence_entry.get()
        position = int(self.position_entry.get())
        nucleotide = self.nuc_clicked.get()

        if mut_type == "Insertion":
            new_sequence = insertion(sequence, position, nucleotide)
            self.master.switch_entry_text(self.new_sequence_box, new_sequence)
        elif mut_type == "Substitution":
            new_sequence = substitution(sequence, position, nucleotide)
            self.master.switch_entry_text(self.new_sequence_box, new_sequence)
        elif mut_type == "Deletion":
            new_sequence = deletion(sequence, position)
            self.master.switch_entry_text(self.new_sequence_box, new_sequence)


mutate_text = """
Paste your DNA sequence in the text box below and select the type of 
mutation. If you leave the location blank, a random location will be
chosen. If no mutation type is chosen, 
"""