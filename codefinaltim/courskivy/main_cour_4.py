import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



class MyGrid(Widget): 
         name = ObjectProperty(None)
         email = ObjectProperty(None)

         def btn(self):
            print("Name: ", self.name.text, "email", self.email.text)
            self.name.text = ""
            self.email.text = ""


         



     

class MyApp(App):
        def build(self):
            return MyGrid()
            
if __name__ == "__main__" :  
        MyApp().run()
    


#le my.kv relatif au cours
# <MyGrid>

#     name: name
#     email: email

#     GridLayout:
#         cols:1
#         size: root.width-200, root.height-200
#         pos: 100, 100

#         GridLayout:
#             cols:2

#             Label : 
#                 text: "Name : "

#             TextInput: 
#                 id: name
#                 multinline:False

#             Label: 
#                 text:"Email: "
#             TextInput: 
#                 id:email
#                 multiline:False

#         Button: 
#             text:"Submit"
#             on_press: root.btn()