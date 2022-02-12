import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class my_grid(GridLayout): 
         def __init__(self, **kwargs):
            super(my_grid, self).__init__(**kwargs)

            self.inside = GridLayout()
            self.inside.cols = 2

            self.cols = 1


            self.inside.add_widget(Label(text="first Name : "))
            self.name = TextInput(multiline=False)
            self.inside.add_widget(self.name)

            self.inside.add_widget(Label(text="last Name : "))
            self.last_name = TextInput(multiline=False)
            self.inside.add_widget(self.last_name)

            self.inside.add_widget(Label(text="email Name : "))
            self.email = TextInput(multiline=False)
            self.inside.add_widget(self.email)

            self.add_widget(self.inside)

            self.submit = Button(text = "tabarnak", font_size=40)
            self.submit.bind(on_press=self.pressed)
            self.add_widget(self.submit)


         def pressed(self,instance):
            name = self.name.text
            last = self.last_name.text
            email = self.email.text

            print("name: ", name)
            self.name.text = ""
            self.last_name.text = ""
            self.email.text = ""


     

class my_app(App):
        def build(self):
            return my_grid()
            
if __name__ == "__main__" :  
        my_app().run()
    