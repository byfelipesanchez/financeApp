from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.button import MDRoundFlatButton
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivymd.uix.tab import MDTabsBase
from database import DataBase
from kivymd.icon_definitions import md_icons
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
Clock.max_iteration = 50




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

                self.manager.current = "login"

            else:
                invalidInfo()
        else:
            invalidInfo()

    def login(self):
        self.reset()
        self.manager.current = "login"

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
            self.manager.current = "main"
        else:
            invalidLogin()

    def create_button(self):
        self.reset()
        self.manager.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    email = ObjectProperty(None)
    created = ObjectProperty(None)
    current = ""

    def log_out(self):
        self.manager.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.password.text = "Password: " + password
        self.created.text = "This Account Was Created On: " + created


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


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


db = DataBase("users.txt")


class MainApp(MDApp):
    icons = list(md_icons.keys())[15:30]
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.theme_cls.theme_style = "Dark"

    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        screens = [LoginWindow(name="login"), AccountWindow(name="create"), MainWindow(name="main")]
        sm = ScreenManager()
        for screen in screens:
            sm.add_widget(screen)
            sm.current = "login"
        return sm

    def __init__(self):
        MainApp.init(self)
        self.iter_list = iter(list(self.icons))


    def on_start(self):
        for name_tab in list(self.icons):
            self.root.ids.tabs.add_widget(Tab(text=name_tab))

    def switch_tab(self):
        '''Switching the tab by name.'''

        try:
            self.root.ids.tabs.switch_tab(next(self.iter_list))
        except StopIteration:
            pass


if __name__ == "__main__":
    MainApp().run()

