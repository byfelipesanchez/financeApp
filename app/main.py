from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.button import MDRectangleFlatButton
# from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
# from kivymd.uix.textfield import MDTextField
from kivy.uix.label import Label
# from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# from helpers import username_helper
# from kivymd.uix.dialog import MDDialog
# from kivy.factory import Factory
# from kivymd.uix.boxlayout import BoxLayout
# # from helpers import KV
# from kivymd.uix.button import MDFloatingActionButtonSpeedDial
# from kivy.uix.screenmanager import Screen, ScreenManager


# class financeApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# class ContentNavigationDrawer(BoxLayout):
#     pass

class Design(GridLayout):
    def __init__(self, **kwargs):
        super(Design, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="name:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)


class App(MDApp):
    # data = {
    #     'currency-usd-off': 'Expense',
    #     'currency-usd': 'Saving'
    #
    # }
    #
    # self.add_widget

    def build(self):
        # self.theme_cls.theme_style = "Dark"  # "Light"
        # return Builder.load_string(KV)
        return Design()

        App().run()
