from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


ALL_GROUPS = 'All groups'
ALL_PROJECTS = 'All projects'


class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

    def set_parameters(self, parent, groups):
        self.groups = groups
        self.controller = parent

        main_layout = GridLayout(rows=3)
        main = BoxLayout(orientation='vertical')
        group_layout = GridLayout(cols=2, padding=10, size=(0, 120), size_hint=(1, None))
        toolbar = BoxLayout(orientation='horizontal', size_hint=(1, .4))

        spinner_groups = Spinner(
            text=ALL_GROUPS, values=[ALL_GROUPS] + [group.name for group in groups],
            size=(0, 50), size_hint=(1, None)
        )
        spinner_groups.bind(text=self.set_group_filter)
        group_layout.add_widget(Label(text="Group :"))
        group_layout.add_widget(spinner_groups)

        self.spinner_projects = Spinner(
            text=ALL_PROJECTS, values=[ALL_PROJECTS],
            size=(0, 50), size_hint=(1, None)
        )
        self.spinner_projects.disabled = True
        self.spinner_projects.bind(text=self.set_project_filter)
        group_layout.add_widget(Label(text="Project :"))
        group_layout.add_widget(self.spinner_projects)

        button_main_start = Button(text='Launch random project')
        button_main_start.bind(on_press=parent.initialize)
        main.add_widget(button_main_start)

        button_toolbar_create_project = Button(text='Create project')
        button_toolbar_create_project.bind(on_press=parent.create_project_window)
        toolbar.add_widget(button_toolbar_create_project)

        button_toolbar_edit_project = Button(text='Edit project')
        button_toolbar_edit_project.bind(on_press=parent.edit_project_window)
        toolbar.add_widget(button_toolbar_edit_project)

        button_toolbar_create_group = Button(text='Create group')
        button_toolbar_create_group.bind(on_press=parent.create_group_window)
        toolbar.add_widget(button_toolbar_create_group)

        button_toolbar_edit_group = Button(text='Edit group')
        button_toolbar_edit_group.bind(on_press=parent.edit_group_window)
        toolbar.add_widget(button_toolbar_edit_group)

        main_layout.add_widget(group_layout)
        main_layout.add_widget(main)
        main_layout.add_widget(toolbar)
        self.add_widget(main_layout)

    def set_group_filter(self, instance, text):
        selected_group = next((group for group in self.groups if group.name == text), None)
        self.controller.set_group_filter(
            selected_group
        )

        self.projects = self.controller.get_projects(selected_group)
        self.spinner_projects.values = [project.name for project in self.projects]
        self.spinner_projects.disabled = selected_group is None
        self.spinner_projects.text = ALL_PROJECTS

    def set_project_filter(self, instance, text):
        selected_project = next((project for project in self.projects if project.name == text), None)
        self.controller.set_project_filter(
            selected_project
        )