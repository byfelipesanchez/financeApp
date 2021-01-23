from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog


class financeApp(MDApp):

    def build(self):
        screen = Screen()

        # username = MDTextField(text='Enter Username',
        #                        pos_hint={'center_x':0.5, 'center_y':0.5 },
        #                        size_hint_x=None, width=300)

        button = MDRectangleFlatButton(text='show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        close_btn = MDRoundFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='User', text=self.username.text,
                               size_hint=(0.7, 1),
                               buttons=[close_btn])
        self.dialog.open()
        # print(self.username.text)

    def close_dialog(self, obj):
        self.dialog.dismiss()


financeApp().run()
