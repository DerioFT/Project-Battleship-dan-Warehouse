import tkinter as tk
from PIL import Image, ImageTk

class ReadyPrompt(tk.Frame):
	def __init__(self, parent, Game):
		self.application = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="slate blue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, height=self.config.height, width=self.config.width, bg="slate blue")
		self.main_frame.pack(expand=True)

		self.ready_msg = tk.Label(self.main_frame, text="Battleship Is Ready!", font=("Arial", 18, "bold"), bg="slate blue", fg="turquoise1")
		self.ready_msg.pack(pady=5)

		image = Image.open(self.config.logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.width
		image = image.resize((int(image_w//ratio//2),int(image_h//ratio//2)))

		self.logo = ImageTk.PhotoImage(image)
		self.center_logo = tk.Label(self.main_frame, image=self.logo)
		self.center_logo.pack(pady=5)

		self.label_msg = tk.Label(self.main_frame, text="Are You Ready?", font=("Arial", 18, "bold"), bg="slate blue", fg="turquoise1")
		self.label_msg.pack(pady=5)

		self.btn_begin = tk.Button(self.main_frame, text="Click here to begin", font=("Arial", 18, "bold"), bg="thistle1", command=lambda:self.application.verify_done())
		self.btn_begin.pack(pady=5)
