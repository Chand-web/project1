from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.screen import Screen


Builder.load_file("bar_with_action.kv")


class Tool_With_Action(Screen):
    title = StringProperty()