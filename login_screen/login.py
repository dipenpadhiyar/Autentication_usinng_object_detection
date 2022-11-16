from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.camera import Image
from kivy.clock import Clock
import time
import cv2

class MainApp(MDApp):
	def build(self):
		self.image = Image()
  
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('login.kv')
	def logger(self):
		self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

	def clear(self):
		self.root.ids.welcome_label.text = "WELCOME"		
		self.root.ids.user.text = ""		
		self.root.ids.password.text = ""

	def capture(self):
		'''
		Function to capture the images and give them the names
		according to their captured time and date.
		'''
		camera = self.ids['camera']
		timestr = time.strftime("%Y%m%d_%H%M%S")
		camera.export_to_png("IMG_{}.png".format(timestr))

print("Captured")	
        
MainApp().run()