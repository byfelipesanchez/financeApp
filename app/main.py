from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class financeApp(MDApp):
    def build(self):
        test = MDLabel(text='sup', halign='center')
        return test

financeApp().run()
