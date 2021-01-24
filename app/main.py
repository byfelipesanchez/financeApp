from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog

# import pyrebase
#
# firebaseConfig = {'apiKey': "AIzaSyA__3SaVDKctOKYRVRyAJGCvFjGcLVp8eI",
#                   'authDomain': "financeapp-bf7c8.firebaseapp.com",
#                   'projectId': "financeapp-bf7c8",
#                   'storageBucket': "financeapp-bf7c8.appspot.com",
#                   'messagingSenderId': "4272125286",
#                   'appId': "1:4272125286:web:1e14d1d14ea5d0a89e44a7",
#                   'measurementId': "G-5K7NJSTM8D"}
#
#
# class auth(object):
#     def auth2(self):
#         firebase = pyrebase.initialize_app(firebaseConfig)
#         user = firebase.auth()
#         self.database_url = firebaseConfig["databaseURL"]
#
#
# def signup():
#     email = input("enter email:")
#     password = input("enter password:")
#     user = auth.create_user_email_and_password(email, password)
#
#
# signup()

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
        if self.username.text is "":
            check_string = 'Please Enter a Username'
        else:
            check_string =  'This Username Does Not Exist'
        close_btn = MDRoundFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='User', text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_btn])
        self.dialog.open()
        # print(self.username.text)

    def close_dialog(self, obj):
        self.dialog.dismiss()



financeApp().run()
