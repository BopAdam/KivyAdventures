import os
os.environ['KIVY_NO_CONSOLELOG'] ='1'

cwd =os.getcwd()
os.environ['KIVY_HOME'] = cwd + '/conf'

# from kivy.config import Config
# Config.set('graphics', 'widht', '1280')
# Config.set('graphics', 'height', '720')
# Config.set('graphics', 'resizable', '0') #1 True >> resizable#
# Config.set('graphics', 'borderless', '0')
#Config.write() => save this attributes int the .kivy config ini file


from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        return Label(text = '[color=ff0000]Hello[/color][color=00ff00]Wolrd[/color]', font_size = 60, italic= True, underline = True, 
                     color=(0.7, 0.5, 0.2,1), bold = True,font_name="./fonts/QuirkyRobot.ttf",markup=True)

    
TestApp().run()