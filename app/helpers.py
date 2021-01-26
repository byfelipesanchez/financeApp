username_helper = """
MDTextField:
    hint_text: "enter username"
    helper_text: "or login"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.5, 'center_y':0.5 }
    size_hint_x: None
"""

KV = '''

Screen

MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Felipe's Finance Tracker"
        left_action_items: [["menu", lambda x:app.callback()]]

    MDLabel:
        text: "Content"
        halign: "center"
    

    
'''

KV = '''

Screen: 

    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True

'''

# KV = '''
#      MDNavigationLayout:
#
#          ScreenManager:
#
#             Screen:
#
#                 BoxLayout:
#                     orientaion:'vertical'
#
#                     MDToolbar:
#                         title: ''
#                         elevation: 10
#                         left_action_items: [['menu, lambda x: nav_drawer.set_state("open")]]
#
#                     widget:
#
#         MDfinanceApp:
#             id: nav_drawer
#
#             ContentNavigationDrawer:
# '''
