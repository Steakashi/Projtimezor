from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

    def set_parameters(self, parent):
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        button_start = Button(text='Hello')
        button_start.bind(on_press=parent.initialize)
        label = Label(text="World'")
        layout.add_widget(button_start)
        layout.add_widget(label)