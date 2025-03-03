import tkinter as tk
from ui.start import StartPage

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
        self._frame.pack()
    
    def close_window(self):
        self.destroy()