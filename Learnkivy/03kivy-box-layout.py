from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class KVBL(BoxLayout):
    pass

class KVBoxLayoutApp(App):
    def build(self):
        return KVBL()

root = KVBoxLayoutApp()
root.run()