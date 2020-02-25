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
        main_layout = GridLayout(rows=2)
        main = BoxLayout(orientation='vertical')
        toolbar = BoxLayout(orientation='horizontal')

        button_main_start = Button(text='Launch random project')
        button_main_start.bind(on_press=parent.initialize)
        main.add_widget(button_main_start)

        button_toolbar_create_project = Button(text='Create project')
        button_toolbar_create_project.bind(on_press=parent.create_project)
        toolbar.add_widget(button_toolbar_create_project)

        button_toolbar_edit_project = Button(text='Edit project')
        button_toolbar_edit_project.bind(on_press=parent.edit_project)
        toolbar.add_widget(button_toolbar_edit_project)

        button_toolbar_create_group = Button(text='Create group')
        button_toolbar_create_group.bind(on_press=parent.create_group)
        toolbar.add_widget(button_toolbar_create_group)

        button_toolbar_edit_group = Button(text='Edit group')
        button_toolbar_edit_group.bind(on_press=parent.edit_group)
        toolbar.add_widget(button_toolbar_edit_group)

        main_layout.add_widget(main)
        main_layout.add_widget(toolbar)
        self.add_widget(main_layout)
