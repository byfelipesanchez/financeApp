from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog
from kivy.factory import Factory
from kivymd.uix.boxlayout import BoxLayout
from helpers import KV
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.uix.screenmanager import Screen, ScreenManager


# class financeApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# class ContentNavigationDrawer(BoxLayout):
#     pass


class financeApp(MDApp):

    data = {
        'currency-usd-off': 'Expense',
        'currency-usd': 'Saving'

    }

    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        return Builder.load_string(KV)



financeApp().run()
