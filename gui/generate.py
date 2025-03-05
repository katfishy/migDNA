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
        153.0,
        anchor="nw",
        text="Number of nucleotides:",
        fill="#1171E3",
        font=("Inter", 20 * -1)
        )

        master.button_images = {
        "generate": tk.PhotoImage(file="./assets/generate_button.png"),
        "homebutton": tk.PhotoImage(file="./assets/home_button.png")
        }

        self.gen_button_image = tk.PhotoImage(
            file=("./assets/generate_button.png"))
        self.generate_button = tk.Button(
            image=self.gen_button_image,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: ,
            relief="flat"
        )
        self.generate_button.place(
            x=18.0,
            y=201.0,
            width=464.0,
            height=65.0
        )

        self.length_image = tk.PhotoImage(
            file="./assets/entry_1.png")
        self.length_bg = self.canvas.create_image(
            250.0,
            205.5,
            image=self.length_image
        )
        self.length_entry = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.length_entry.place(
            x=18.0,
            y=183.0,
            width=464.0,
            height=43.0
        )

        self.new_sequence_box_image = tk.PhotoImage(
            file="./assets/entry_2.png")
        self.new_seq_bg = self.canvas.create_image(
            250.0,
            379.5,
            image=self.new_sequence_box_image
        )
        self.new_sequence_box = tk.Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.new_sequence_box.place(
            x=18.0,
            y=280.0,
            width=464.0,
            height=197.0
        )

        self.canvas.create_text(
            18.0,
            94.0,
            anchor="nw",
            text="Generate a random DNA sequence of\ndesired length.",
            fill="#0B2F59",
            font=("Inter", 20 * -1)
        )

        self.home_image = tk.PhotoImage(
            file="./assets/home_button.png")
        self.home_button = tk.Button(
            image=self.home_image,
            borderwidth=0,
            highlightthickness=0,
            command=master.go_to_start,
            relief="flat",
            bg="white"
        )
        self.home_button.place(
            x=422.0,
            y=21.0,
            width=60.0,
            height=60.0
        )

        # tk.Label(self, text=generate_text).pack(side="top", fill="x", pady=10)

        # input_frame = tk.Frame(self)
        # input_frame.pack(pady=10)

        # tk.Label(self, text="Number of nucleotides").pack(side="left", padx=5)
        # self.Entry = tk.Entry(input_frame, bd=5).pack(side="right", padx=5)
        # tk.Button(self, text="Return to start page",
        #           command=self.go_to_start).pack(pady=10)


generate_text = """
Generate a random DNA sequence of desired length.
"""

def generate_random_sequence(n: int) -> str:
    """Generate a random sequence of n length."""
    nucleotides = ["A", "T", "G", "C"]
    return ''.join(random.choices(nucleotides), k=n)