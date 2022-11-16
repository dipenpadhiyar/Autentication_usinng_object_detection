import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height=40
        self.col_force_default=True
        self.col_default_width=100
        # create second gridlayout
        self.top_grid = GridLayout(row_force_default = True,row_default_height=120,col_force_default=True,   col_default_width=100)
        self.top_grid.cols = 2
        # add widgets1
        self.top_grid.add_widget(Label(text = "Name: "))
        # add input box1
        self.name = TextInput(multiline = False,)
        self.top_grid.add_widget(self.name)
        # add widgets2
        self.top_grid.add_widget(Label(text = "Middule name: "))
        # add input box2
        self.mid_name= TextInput(multiline = False)
        self.top_grid.add_widget(self.mid_name)
        # add widgets3
        self.top_grid.add_widget(Label(text = "Surname: "))
        # add input box3
        self.surname = TextInput(multiline = False)
        self.top_grid.add_widget(self.surname)
        
        self.add_widget(self.top_grid)
        # create submit button
        self.submit = Button(text = "Submit",
                             font_size = 32,
                             size_hint_y = None,
                             height = 100,
                             size_hint_x = None,
                             width = 200
                             )
        # Bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
    
    def press(self,instance):
        name = self.name.text
        middName=self.mid_name.text
        surName=self.surname.text
        
        # print()
        if name and middName and surName != "":
            self.add_widget(Label(text = f"your full name is {name} {middName} {surName}."))
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