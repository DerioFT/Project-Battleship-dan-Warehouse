import tkinter as tk
from tkinter import *
import sys

from config import Config
from ship import Ship
from player import Player
from board import Board
from ready_prompt import ReadyPrompt
from login_prompt import Login
from win_prompt import Win

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)

		self.create_menu_bar()

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_ready_prompt()
		self.create_login_menu()

	def create_menu_bar(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
		self.fileMenu.add_command(label="Exit", command=self.exit_on_click)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=self.about)

		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill= "both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_ready_prompt(self):
		self.pages["ready_prompt"] = ReadyPrompt(self.container, self)

	def verify_done(self):
		self.change_page("board")

	def create_login_menu(self):
		self.pages["login_prompt"] = Login(self.container, self)

	def congratulations(self):
		self.pages["win_prompt"] = Win(self.container, self)

	def terminate(self):
		sys.exit()

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def verify_login(self):
		username = self.pages["login_prompt"].var_username.get()
		password = self.pages["login_prompt"].var_password.get()


		granted = self.config.check_login_info(username, password)
		if granted:
			self.change_page("ready_prompt")
		else:
			self.login_error()

	def exit_on_click(self):

		exit_popup = Toplevel(self)
		exit_popup.title(self.config.exit_popup_title)
		exit_popup.geometry(self.config.exit_popup_window)
		exit_popup.configure(bg="gold")

		label = Label(exit_popup, text="Are You Sure To Exit?", bg="yellow", fg="red", font=("Arial", 12, "bold"))
		label.pack(pady=10)

		exit_popup_frame = Frame(exit_popup, bg="gold")
		exit_popup_frame.pack(pady=5)

		yes_button = Button(exit_popup_frame, text="YES", font=("Arial", 10, "bold"), fg="red2", command=self.terminate)
		yes_button.grid(row=0, column=1, padx=5)

		no_button = Button(exit_popup_frame, text=" NO ", font=("Arial", 10, "bold"), fg="blue2", command=exit_popup.destroy)
		no_button.grid(row=0, column=2, padx=5)

	def about(self):

		about_popup = Toplevel(self)
		about_popup.title(self.config.about_popup_title)
		about_popup.geometry(self.config.about_popup)
		about_popup.config(bg="plum")

		label = Label(about_popup, text=self.config.about_msg, bg="plum", fg="slateblue2", font=("Arial", 10 , "bold"))
		label.pack()

		about_popup_frame = Frame(about_popup, bg="plum")
		about_popup_frame.pack()

		close_button = Button(about_popup_frame, text="Close", fg="red", font=("Arial", 10, "bold"), command=about_popup.destroy)
		close_button.grid(row=1, column=2, pady=5)

	def login_error(self):

		login_error = Toplevel(self)
		login_error.title(self.config.login_error_popup_title)
		login_error.geometry(self.config.login_error_popup)
		login_error.config(bg="#ab4302")

		label = Label(login_error, text="USERNAME OR PASSWORD IS WRONG!!", bg="#ab4302", fg="#abea02", font=("Arial", 10 , "bold"))
		label.pack()

		login_error_frame = Frame(login_error, bg="#ab4302")
		login_error_frame.pack()

		close_button = Button(login_error_frame, text="Close", fg="red", font=("Arial", 10, "bold"), command=login_error.destroy)
		close_button.grid(row=1, column=2, pady=5)

class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages["board"].change_img_button(pos_x, pos_y, win)
		if win:
			print(f"Congratulations, You Win !!")
			
			self.window.congratulations()

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()
