import tkinter as tk
from gui.mutate import Mutate
from gui.identify import Identify 
from gui.generate import Generate

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
            font=("Inter", 48 * -1, 'bold')
        )

        # Adding the DNA Image
        self.image_1 = tk.PhotoImage(file="./assets/image_1.png")
        self.canvas.create_image(250.0, 169.0, image=self.image_1)

        # Load button images (normal and hover states)
        master.button_images = {
            "mutate": tk.PhotoImage(file="./assets/button_1.png"),
            "mutate_hover": tk.PhotoImage(file="./assets/button_hover_1.png"),
            "identify": tk.PhotoImage(file="./assets/button_2.png"),
            "identify_hover": tk.PhotoImage(file="./assets/button_hover_2.png"),
            "generate": tk.PhotoImage(file="./assets/button_3.png"),
            "generate_hover": tk.PhotoImage(file="./assets/button_hover_3.png"),
        }

        # Create buttons
        master.create_button(self, "mutate", 136, 137, 18, 346, master.switch_frame, Mutate)
        master.create_button(self, "identify", 136, 137, 182, 346, master.switch_frame, Identify)
        master.create_button(self, "generate", 136, 137, 346, 346, master.switch_frame, Generate)