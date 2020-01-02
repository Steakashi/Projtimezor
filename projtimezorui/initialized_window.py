from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
import datetime
import time


class InitializedScreen(Screen):

    def __init__(self, **kwargs):
        super(InitializedScreen, self).__init__(**kwargs)

        self.main_layout = GridLayout(rows=2)
        self.project_layout = BoxLayout(orientation='vertical')
        self.toolbar_layout = BoxLayout(orientation='horizontal')
        self.main_layout.add_widget(self.project_layout)
        self.main_layout.add_widget(self.toolbar_layout)

        self.add_widget(self.main_layout)

    def get_initialized_datetime(self):
        return self.clock_beginning

    def set_parameters(self, parent, project, step):
        label_project = Label(text=project.name)
        label_step = Label(text=step.description)
        self.project_layout.add_widget(label_project)
        self.project_layout.add_widget(label_step)

        button_pause = Button(text='Hello')
        button_pause.bind(on_press=parent.pause)
        self.toolbar_layout.add_widget(Label(text='test 1'))
        self.toolbar_layout.add_widget(Label(text='test 2'))

        self.label_time = Label(text='0')
        self.toolbar_layout.add_widget(self.label_time)
        self.clock_beginning = datetime.datetime.now()
        Clock.schedule_interval(parent.calculate_elapsed_time, .1)

    def set_label_elapsed_time(self, hours, minutes, seconds):
        self.label_time.text = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
