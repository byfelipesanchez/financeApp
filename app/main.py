from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivy.uix.label import Label
# from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty



class Design(Widget):
    test: ObjectProperty(None)

    def btn(self):
        print("test", self.test.text)
        self.test.text = " "


class FinanceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        # return Builder.load_string(KV)
        return Design()

FinanceApp().run()
