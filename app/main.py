from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from database import DataBase
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.properties import OptionProperty


class AccountWindow(Screen):
    name1 = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)

    def submit(self):
        if self.name1.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                db.add_user(self.email.text, self.password.text, self.name1.text)

                self.reset()

                sm.current = "login"

            else:
                invalidInfo()
        else:
            invalidInfo()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.name1.text = ""
        self.email.text = ""
        self.password.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_button(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def create_button(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n: ObjectProperty(None)
    email: ObjectProperty(None)
    created: ObjectProperty(None)
    current = ""

    def log_out(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.password.text = "Password: " + password
        self.created.text = "This Account Was Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidInfo():
    pop = Popup(title="Invalid Information", content=Label(text="Please Fill All The Required Inputs"),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidLogin():
    pop = Popup(title="Invalid Login", content=Label(text="The Entered Username or Password is Incorrect"),
                size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), AccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyFinanceApp(App):

    media = OptionProperty('M', options=('XS', 'S', 'M', 'L', 'XL'))

    def build(self):
        Window.bind(size=self.update_media)
        return sm
        # self.theme_cls.theme_style = "Dark"  # "Light"


    def update_media(self, win, size):
        width, height = size
        self.media = (
            'XS' if width < 250 else
            'S' if width < 500 else
            'M' if width < 1000 else
            'L' if width < 1200 else
            'XL'
        )


if __name__ == "__main__":
    MyFinanceApp().run()

