
import self as self
import sm as sm
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from database import DataBase


class AccountWindow(Screen):
    name1 = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)

    def submit(self):
        if self.name1.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                self.reset()

                sm.current = "login"
            else:
                invalidInfo()

    def login(self):
        self.reset()
        sm.current


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginButton(self):
        if db.validation(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidInfo()

    def createButton(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.name1.text = ""
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n: ObjectProperty(None)
    email: ObjectProperty(None)
    createdDate: ObjectProperty(None)

    def log_out(self):
        sm.current("login")

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name " + name
        self.email.text = "Email " + self.current
        self.password.text = "Password " + password
        self.created.text = "This Account Was Created On " + created


class WindowManager(ScreenManager):
    pass


def invalidInfo():
    popup = Popup(title="Invalid Information",
                  content=Label(text="The Entered Username or Password is Incorrect"),
                  size_hint=(None, None), size=(400, 400))
    popup.open()


kv = Builder.load_file("finance.kv")

sm = WindowManager()
db = DataBase("users.txt")
screens: [LoginWindow(name="login"), AccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class FinanceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        return sm


FinanceApp().run()
