import self as self
import sm as sm
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class AccountWindow(Screen):
    name1 = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)

    def submit(self):
        if self.name1.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                #todo: add user to data base
                self.reset()

                sm.current = "login" #todo: into login window
            else:
                invalidInfo() #todo: crate invalidInfo method

    def login(self):
        self.reset()
        sm.current

    def reset(self):
        self.name1.text = ""
        self.email.text = ""
        self.password.text = ""


class loginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginButton(self):

        #todo: validation on database

class mainWindow(Screen):
    accname: ObjectProperty(None)
    email: ObjectProperty(None)
    createdDate: ObjectProperty(None)

    def logOut(self):
        sm.current("login")

    #todo: def a 'subwindow' for when you enter displaying you info

class WindowManager(ScreenManager):
    pass

def invalidInfo() #todo: as a popUp

kv = Builder.load_file("finance.kv")

sm = WindowManager()
#todo: database

screens: [#todo]

class FinanceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        # return Builder.load_string(KV)
        return kv

FinanceApp().run()
