from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,CardTransition,SlideTransition
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
import random

Builder.load_file("app_design.kv")



class MainScreen(Screen):
    def funtc(self):
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        self.ids.img_1.source='Images\{}.png'.format(num1)
        self.ids.img_2.source='Images\{}.png'.format(num2)

            
            

    pass




class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        Window.clearcolor=(0/255,0/255,0/255,1)
        return RootWidget()



if __name__=='__main__':
    MainApp().run()