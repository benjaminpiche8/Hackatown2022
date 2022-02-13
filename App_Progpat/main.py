# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import datetime 

from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import datetime
#from codefinaltim.App_Progpat.database import DataBase # USEFUL FOR DATABASE **************************************

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import meteo as mt
import outfit as of

# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.icon = mt.get_current_icon()



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

    dateToday = str(datetime.date.today())
    dateTomorrow = str(datetime.date.today() + datetime.timedelta(days = 1))

    condLetter = mt.get_current_condition()
    condTodMin =  str(mt.get_daily_forecast_raw_temp('c','min', dateToday))
    condTodMax =  str(mt.get_daily_forecast_raw_temp('c','max', dateToday))
    condIcon = mt.get_daily_forecast_icon(dateToday)
    CondLive = mt.get_current_feelslike_temp('c')

    condTomMin = str(mt.get_daily_forecast_raw_temp('c','min', dateTomorrow ))
    condTomMax = str(mt.get_daily_forecast_raw_temp('c','max', dateTomorrow ))

    rain = mt.will_it_rain(dateToday)
    snow = mt.will_it_snow(dateToday)
  


    def homeBtn(self):
        screenManager.current = "main"

    def settingsBtn(self):
        screenManager.current = "settings"    
    
    def outfitBtn(self):
        screenManager.current = "outfit"  


#WINDOW SUR LA PAGE DE OUTFIT
class FullOutfitPage(Screen):
    dateToday = str(datetime.date.today())
    dateTomorrow = str(datetime.date.today() + datetime.timedelta(days = 1))
    __icon__ = mt.get_daily_forecast_icon(dateToday)
    __recommended_top__ = of.short_term_recommandation_top()
    #__recommended_bottom__ = of.short_term_recommandation_bottom('m')
    #__recommended_footwear__ = 



    def homeBtn(self):
        screenManager.current = "main"  

    def settingsBtn(self):
        screenManager.current = "settings"    

    def meteoBtn(self):
        screenManager.current = "meteo"

    def build(self):
        Window.clearcolor(1,1,1,1)

    
   # def on_enter(self):
    #    App.GetIcon().icon =  mt.get_current_condition()
class MyGrid(Widget):
    pass

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
    print(mt.get_current_condition())
    print(mt.get_current_icon())






