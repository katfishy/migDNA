import tkinter as tk
import random

class Generate(tk.Frame):
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
            text="Generate",
            fill="#0B2F59",
            font=("Inter", 48 * -1, 'bold')
        )

        self.canvas.create_text(
        17.0,
        163.0,
        anchor="nw",
        text="Number of nucleotides:",
        fill="#1171E3",
        font=("Inter", 20 * -1)
        )

        master.button_images = {
        "generate": tk.PhotoImage(file="./assets/generate_button.png"),
        "generate_hover": tk.PhotoImage(file="./assets/generate_button.png"),
        "homebutton": tk.PhotoImage(file="./assets/home_button.png"),
        "homebutton_hover": tk.PhotoImage(file="./assets/home_button.png")
        }

        master.create_button(self, "generate", 464, 65, 18, 201, self.generate_random_sequence)
        master.create_button(self, "homebutton", 60, 60, 422, 21, master.go_to_start)

        self.user_input = tk.StringVar()
        self.length_image = tk.PhotoImage(
            file="./assets/entry_1.png")
        self.length_bg = self.canvas.create_image(
            250.0,
            215.5,
            image=self.length_image
        )
        self.length_entry = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=3,
            textvariable=self.user_input,
            font=("Inter", 16 * -1),
            relief="solid",
            highlightcolor="#1172E3",
            highlightbackground="#1172E3"
        )
        self.length_entry.place(
            x=18.0,
            y=193.0,
            width=464.0,
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

        self.canvas.create_text(
            18.0,
            85.0,
            anchor="nw",
            text=generate_text,
            fill="#0B2F59",
            font=("Inter", 16 * -1)
        )

    def generate_random_sequence(self):
        """Generate a random sequence of n length."""
        nucleotides = ["A", "T", "G", "C"]
        length = self.length_entry.get()
        if length.isnumeric():
            new_sequence = ''.join(random.choices(nucleotides, k=int(length)))
            self.new_sequence_box.config(state="normal")
            self.new_sequence_box.delete("1.0", tk.END)
            self.new_sequence_box.insert("1.0", new_sequence)
            self.new_sequence_box.config(state="disabled")

        else:
            self.new_sequence_box.config(state="normal")
            self.new_sequence_box.delete("1.0", tk.END)
            self.new_sequence_box.insert("1.0", "Error - input numerical values only.")
            self.new_sequence_box.config(state="disabled")


generate_text = """
Generate a random DNA sequence of\ndesired length.
"""

