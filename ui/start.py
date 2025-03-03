import tkinter as tk
from ui.mutate import Mutate
from ui.identify import Identify 
from ui.generate import Generate

class StartPage(tk.Frame):
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
            text="migDNA",
            fill="#0B2F59",
            font=("Inter Bold", 48 * -1)
        )

        # Adding the DNA Image
        self.image_1 = tk.PhotoImage(file="./assets/image_1.png")
        self.canvas.create_image(250.0, 169.0, image=self.image_1)

        # Load button images (normal and hover states)
        self.button_images = {
            "mutate": tk.PhotoImage(file="./assets/button_1.png"),
            "mutate_hover": tk.PhotoImage(file="./assets/button_hover_1.png"),
            "identify": tk.PhotoImage(file="./assets/button_2.png"),
            "identify_hover": tk.PhotoImage(file="./assets/button_hover_2.png"),
            "generate": tk.PhotoImage(file="./assets/button_3.png"),
            "generate_hover": tk.PhotoImage(file="./assets/button_hover_3.png"),
        }

        # Create buttons
        self.create_button("mutate", 18, 346, master.switch_frame, Mutate)
        self.create_button("identify", 182, 346, master.switch_frame, Identify)
        self.create_button("generate", 346, 346, master.switch_frame, Generate)

    def create_button(self, name, x, y, command, target_frame):
        """Helper function to create buttons with hover effects."""
        button = tk.Button(
            self,
            bg="white",
            image=self.button_images[name],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: command(target_frame),
            relief="flat"
        )
        button.place(x=x, y=y, width=136, height=137)

        # Add hover effects
        button.bind('<Enter>', lambda e: button.config(image=self.button_images[f"{name}_hover"]))
        button.bind('<Leave>', lambda e: button.config(image=self.button_images[name]))