# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

#from codefinaltim.App_Progpat.database import DataBase # USEFUL FOR DATABASE **************************************


#WINDOW  SUR  LA PAGE PRINCIPALE
class HomePage(Screen):  #self.reset() may be important
    def settingsBtn(self):
        screenManager.current = "settings"    

    def meteoBtn(self):
        screenManager.current = "meteo"

    def outfitBtn(self):
        screenManager.current = "outfit"     


# WINDOW SUR LA PAGE DE SETTINGS
class SettingsPage(Screen):
    def homeBtn(self):
        screenManager.current = "main"    

    def meteoBtn(self):
        screenManager.current = "meteo"

    def outfitBtn(self):
        screenManager.current = "outfit"  


#WINDOW SUR LA PAGE DE MÉTÉO COMPLÈTE
class FullMeteoPage(Screen):
    
    #condition = ObjectProperty(None)
    condition = meteo.get_current_condition()
    

    def homeBtn(self):
        screenManager.current = "main"

    def settingsBtn(self):
        screenManager.current = "settings"    
    
    def outfitBtn(self):
        screenManager.current = "outfit"  


#WINDOW SUR LA PAGE DE OUTFIT
class FullOutfitPage(Screen):
    def homeBtn(self):
        screenManager.current = "main"  

    def settingsBtn(self):
        screenManager.current = "settings"    

    def meteoBtn(self):
        screenManager.current = "meteo"

    

class WindowManager(ScreenManager):             #S'OCCUPE DE GÉRER LES MULTIPLES WINDOW (LES CHANGER QUAND NÉCÉSSAIRE)
    pass


def invalidLogin(): #AS TO BE CALLED SOMEWHERE TO BE USEFUL**** IP ADRESS
    pop = Popup(title='NOTIFICATION!',
                  content=Label(text='WE ARE ABOUT TO USE UR LOCATION :)'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()



kv = Builder.load_file("my.kv")

screenManager = WindowManager()
#db = DataBase("users.txt")                     #USEFULL FOR DATABASE PURPOSES !

screens = [HomePage(name="main"), SettingsPage(name="settings"), FullMeteoPage(name="meteo"), FullOutfitPage(name="outfit")]
for screen in screens:
    screenManager.add_widget(screen)

screenManager.current = "main"


class MyMainApp(App):
    def build(self):
        return screenManager


if __name__ == "__main__":
    MyMainApp().run()






