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


# class financeApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# class ContentNavigationDrawer(BoxLayout):
#     pass


class financeApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


financeApp().run()
