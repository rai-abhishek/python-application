import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyfirstKivyApp(App):
    def build(self):
        return Label(text='Hello World')


t = MyfirstKivyApp()
t.run()
