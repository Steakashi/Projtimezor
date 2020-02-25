from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


FIELDS = [
    "Name",
    "Description",
    "Priority",
    "Group",

]


class CreateProjectWindow(Screen):

    def __init__(self, **kwargs):
        super(CreateProjectWindow, self).__init__(**kwargs)

        main_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        for field in FIELDS:
            main_layout.add_widget(Label(text=field))
            main_layout.add_widget(TextInput(text=field.lower(), multiline=False))

        self.add_widget(main_layout)
