from kivymd.app import MDApp

from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager



class MyScreenManager(NavigationScreenManager):
    pass





class ComputerApp(MDApp):
    manager = ObjectProperty(None)

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"

        self.manager = MyScreenManager()
        return self.manager 
    
    
    
    

ComputerApp().run()
        
        
        
        