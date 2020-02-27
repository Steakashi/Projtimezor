from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


FIELDS = [
    "name",
    "description",
    "priority",
    "group",
]


class CreateProjectWindow(Screen):

    def __init__(self, **kwargs):
        super(CreateProjectWindow, self).__init__(**kwargs)

        self.main_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        self.inputs = list()
        for field in FIELDS:
            self.main_layout.add_widget(Label(text=field.capitalize()))
            text_input = TextInput(text=field, multiline=False)
            self.inputs.append(text_input)
            self.main_layout.add_widget(text_input)

        self.add_widget(self.main_layout)

    def set_parameters(self, parent):
        button_create = Button(text='Create')
        button_create.fbind(
            'on_press',
            parent.create_project,
            {FIELDS[count]: input_.text for count, input_ in enumerate(self.inputs)}
        )

        self.main_layout.add_widget(Widget())
        self.main_layout.add_widget(button_create)