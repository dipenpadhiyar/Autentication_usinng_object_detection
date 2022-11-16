import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_file("my.kv")
    
class MyGridLayout(Widget):
    # initialize infinite keywords
    name = ObjectProperty(None)
    mid_name = ObjectProperty(None)
    surname = ObjectProperty(None)
    labeloutput = ObjectProperty(None)
    
    
    def press(self):
        name = self.name.text
        mid_name=self.mid_name.text
        surname=self.surname.text
        labeloutput =self.labeloutput.text
        
        # print()
        if name and mid_name and surname != "":
            print(f"your full name is {name} {mid_name} {surname}.")
            labeloutput =  Label(text = f"your full name is {name} {mid_name} {surname}.")
        # clear input boxes
        else:
            self.name.text=""
            self.mid_name.text=""
            self.surname.text=""
        self.name.text=""
        self.mid_name.text=""
        self.surname.text=""
class MyApp(App):
    def build(self):
        #  creating Floatlayout
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()