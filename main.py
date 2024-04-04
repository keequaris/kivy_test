from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import OptionProperty
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random

Window.size=(480,853)

from kivymd.theming import ThemeManager

class Container(GridLayout):
    def action(self):
        self.one.text=str(random.randint(0,100))


class MainApp(App):
    theme_cls=ThemeManager()
    def build(self):
        self.theme_cls.theme_style='Light'
        return Container()

if __name__=='__main__':
    MainApp().run()
