# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#from codefinaltim.App_Progpat.database import DataBase # USEFUL FOR DATABASE **************************************


# class CreateAccountWindow(Screen):
#     namee = ObjectProperty(None)
#     email = ObjectProperty(None)
#     password = ObjectProperty(None)

#     def submit(self):
#         if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
#             if self.password != "":
#                 db.add_user(self.email.text, self.password.text, self.namee.text)

#                 self.reset()

#                 secreenManager.current = "login"
#             else:
#                 invalidForm()
#         else:
#             invalidForm()

#     def login(self):
#         self.reset()
#         secreenManager.current = "login"

#     def reset(self):
#         self.email.text = ""
#         self.password.text = ""
#         self.namee.text = ""


# class LoginWindow(Screen):
#     email = ObjectProperty(None)
#     password = ObjectProperty(None)

#     def loginBtn(self):
#         if db.validate(self.email.text, self.password.text):
#             MainWindow.current = self.email.text
#             self.reset()
#             secreenManager.current = "main"
#         else:
#             invalidLogin()

#     def createBtn(self):
#         self.reset()
#         secreenManager.current = "create" #fonction pour changer d'un window à l'autre*****************************************************************

#     def reset(self):
#         self.email.text = "" 
#         self.password.text = ""



# class MainWindow(Screen):
#     n = ObjectProperty(None)
#     created = ObjectProperty(None)
#     email = ObjectProperty(None)
#     current = ""

#     def logOut(self):
#         secreenManager.current = "login"

#     def on_enter(self, *args):
#         password, name, created = db.get_user(self.current)
#         self.n.text = "Account Name: " + name
#         self.email.text = "Email: " + self.current
#         self.created.text = "Created On: " + created

class HomePage(Screen):
    def settingsBtn(self):
        screenManager.current = "create"    

    def meteoBtn(self):
        screenManager.current = "main"

    def outfitBtn(self):
        screenManager.current = "create"     



class SettingsPage(Screen):
    pass

class FullMeteoPage(Screen):
    pass

class FullOutfitPage(Screen):
    pass





class WindowManager(ScreenManager): #S'OCCUPE DE GÉRER LES MULTIPLES WINDOW (LES CHANGER QUAND NÉCÉSSAIRE)
    pass


def invalidLogin(): #AS TO BE CALLED SOMEWHERE TO BE USEFUL**** IP ADRESS
    pop = Popup(title='NOTIFICATION!',
                  content=Label(text='WE ARE ABOUT TO USE UR LOCATION :)'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()



kv = Builder.load_file("my.kv")

screenManager = WindowManager()
#db = DataBase("users.txt")                 #USEFULL FOR DATABASE PURPOSES !

screens = [HomePage(name="main"), SettingsPage(name="settings"), FullMeteoPage(name="meteo"), FullOutfitPage(name="outfit")]
for screen in screens:
    screenManager.add_widget(screen)

screenManager.current = "main"


class MyMainApp(App):
    def build(self):
        return screenManager


if __name__ == "__main__":
    MyMainApp().run()






