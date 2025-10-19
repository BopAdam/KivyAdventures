import os
os.environ['KIVY_NO_CONSOLELOG'] ='1'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class AlapWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gomb1= Button(text="Gomb 1", size_hint=(None, None), size=(100,50), pos=(0,0))
        gomb1.custom_id = "gomb1"
        gomb1.bind(on_press=self.hello_gomb)
        self.add_widget(gomb1)

        gomb2=Button(text="Gomb 2", size_hint=(None, None), size=(100,50), pos=(100,100))
        gomb2.custom_id = "gomb2"
        gomb2.bind(on_press=self.hello_gomb)
        self.add_widget(gomb2)

    def hello_gomb(self, instance):
        if instance.custom_id == "gomb1":
            print("Hello Gomb1")
        elif instance.custom_id == "gomb2":
            print("Hello Gomb2")

class TestApp(App):
    def build(self):
        return AlapWidget()

if __name__ == '__main__':
    TestApp().run()
