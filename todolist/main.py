#! -*- coding:utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('main.kv')

class LayoutApp(Screen):
    pass


class HomeApp(App):
    def build(self):
        return LayoutApp()
    # pass





if __name__ == '__main__':
    HomeApp().run()