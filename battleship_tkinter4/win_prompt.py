import tkinter as tk
from PIL import Image, ImageTk

class Win(tk.Frame):
	def __init__(self, parent, Game):
		self.application = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="salmon1")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, height=self.config.height, width=self.config.width, bg="salmon1")
		self.main_frame.pack(expand=True)

		self.congratulations_msg = tk.Label(self.main_frame, text="CONGRATULATIONS", font=("helvetica", 18, "bold"), bg="salmon1", fg="darkslategray2")
		self.congratulations_msg.pack(pady=5)


		image = Image.open(self.config.ending_img_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.width
		image = image.resize((int(image_w//ratio//2),int(image_h//ratio//2)))

		self.logo = ImageTk.PhotoImage(image)
		self.center_logo = tk.Label(self.main_frame, image=self.logo)
		self.center_logo.pack(pady=5)

		self.label_msg = tk.Label(self.main_frame, text="YOU WIN !!!", font=("helvetica", 18, "bold"), bg="salmon1", fg="darkslategray2")
		self.label_msg.pack(pady=5)

		self.btn_exit = tk.Button(self.main_frame, text="Click here to exit", font=("helvetica", 18, "bold"), bg="black", fg="light pink", command=lambda:self.application.terminate())
		self.btn_exit.pack(pady=5)

		
