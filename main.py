from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.image import Image
from kivymd.color_definitions import colors
from kivymd.uix.textfield import MDTextField

Window.size = (360, 750)

KV = '''
MDBoxLayout:
    orientation: "vertical"
    

    FitImage:
        size_hint_y: 3
        source: 'images/vboy.png'
        
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(KV)


Main().run()