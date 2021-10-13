import first as first
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.window import Window


class MyApp(App):

    def build(self):
        window_sizes = Window.size

        return Label(text="height & width = " + str(window_sizes))


MyApp().run()
