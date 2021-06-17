import sys
from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from login_prompt import Login
from settings import Settings
from appPage import AppPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_menus()

		self.create_container()

		self.pages = {}
		self.create_appPage()
		self.create_login_menu()

	def create_login_menu(self):
		self.pages["login_prompt"] = Login(self.container, self)

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def verify_login(self):
		username = self.pages["login_prompt"].var_username.get()
		password = self.pages["login_prompt"].var_password.get()


		granted = self.settings.check_login_info(username, password)
		if granted:
			self.change_page("appPage")
		else:
			msg.showerror("Error", "Username or Password is wrong !!!")

	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
		#self.fileMenu.add_command(label="New Item")
		#self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Sign Out", command=self.sign_out)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Exit", command=self.exit_program)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=self.show_about_info)

		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)


	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)

	def show_about_info(self):
		msg.showinfo("About Storage App", "This app is created by Derio Fernand Teddy\n\n~Copyright-2021")
		#msg.showwarning("About Contact App", "This apps created by\n1. Ali\n2. Budi\n\nCopyright-2021")
		#msg.showerror("About Contact App", "This apps created by\n1. Ali\n2. Budi\n\nCopyright-2021")

	def countdown_timer(self):
		respond = msg.askyesnocancel("Last Warning", "This app will close in 3 seconds after you click Yes")
		if respond:
			self.after(3000, self.terminate)

	def terminate(self):
		sys.exit()

	def exit_program(self):
		respond = msg.askyesnocancel("Exit Program", "Are you sure and really sure to close the program ?")
		if respond:
			self.countdown_timer()

	def sign_out(self):
		respond = msg.askyesnocancel("Exit Program", "Are you sure and really sure to sign out ?")
		if respond:
			self.create_login_menu()

class StorageApp:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myStorageApp = StorageApp()
	myStorageApp.run()