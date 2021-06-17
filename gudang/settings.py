from json import load, dump
import json
class Settings:

	def __init__(self):

		#APP CONF
		self.title = "Gudang"


		#WINDOW CONF
		base = 75
		ratio = (12, 6)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+150+50"

		#LOGIN WINDOW CONFIG
		#self.login_window = self.screen

		#IMG CONF
		self.logo = "img/logo_gudang.jpeg"
		self.login_logo_path = "img/login_img.png"

		#LOGIN DATA PATH
		self.user_account = "users_account.json"

		#self.contacts = None
		self.load_data_from_json()


	def load_data_from_json(self):
		with open("data/item.json", "r") as file_json:
			self.items = load(file_json)

	def save_data_to_json(self):
		with open("data/item.json", "w") as file_json:
			dump(self.items, file_json)

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
