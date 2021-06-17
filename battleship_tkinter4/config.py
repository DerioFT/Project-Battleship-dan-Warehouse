import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"

		#GAME CONFIG

		self.row = 5
		self.column = 5

		#WINHDOW CONFIG
		base = 100
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+100"

		#LOGIN WINDOW CONFIG
		self.width = base*3
		self.height = base*4
		
		#LOGIN ERROR POPUP CONFIG
		self.login_error_popup = "400x70+550+350"
		self.login_error_popup_title = "Alert"

		#ABOUT POPUP CONFIG
		self.about_popup = "400x70+550+350"
		self.about_popup_title = "About"

		self.about_msg = "Aplikasi ini pertama kali dibuat pada tanggal 18 Maret 2021"

		#EXIT POPUP CONFIG
		self.exit_popup_window = "250x100+630+300"
		self.exit_popup_title = "Exit?"

		#LOGIN DATA PATH
		self.user_account = "users_account.json"

		#LOGIN IMG PATH
		self.login_logo_path = "img/login_img.png"

		#PROMPT IMG PATH
		self.logo_path = "img/logo.png"

		#WIN IMG PATH
		self.ending_img_path = "img/win_logo.png"
		
		#IMG BUTTON PATH
		self.init_img_btn = "img/init_img.png"
		self.final_img_btn = "img/final_img.png"
		self.win_img_btn = "img/win_img.jpg"

	def load_data(self, path):
		with open(path, "r") as json_data:
			data = json.load(json_data)
		return data

	def check_login_info(self, username, password):
		check_user = self.load_data(self.user_account)
		if username in check_user:
			if password == check_user[username]["password"]:
				return True
			else:
				return False
		else:
			return False