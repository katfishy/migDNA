import tkinter as tk
from gui.start import StartPage

class MutationSim(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x500")
        self.configure(bg = "#FFFFFF")
        self.title('migDNA')

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

    def create_button(self, parent, name, x, y, command, target_frame):
        """Helper function to create buttons with hover effects."""
        button = tk.Button(
            parent,
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
    
    def close_window(self):
        self.destroy()

    def go_to_start(self):
        self.switch_frame(StartPage)