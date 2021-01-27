from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class MainWindow(Screen):
    pass

    def Widgets(Widgets):
        pass


class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("finance.kv")

class FinanceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        # return Builder.load_string(KV)
        return kv

FinanceApp().run()
