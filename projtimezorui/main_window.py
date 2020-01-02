import datetime


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


from .start_window import StartScreen
from .initialized_window import InitializedScreen
from projtimezor.constants import START_SCREEN, INITIALIZED_SCREEN


class MainWindow(App):

    def __init__(self, parent, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.app = parent
        self.screen_manager = ScreenManager()
        self.screens = dict()

        self.screens[START_SCREEN] = StartScreen(name='1')
        self.screens[START_SCREEN].set_parameters(parent=self)
        self.screen_manager.add_widget(self.screens[START_SCREEN])

        self.screens[INITIALIZED_SCREEN] = InitializedScreen(name='2')
        self.screen_manager.add_widget(self.screens[INITIALIZED_SCREEN])

    def build(self):
        return self.screen_manager

    def initialize(self, instance):
        self.app.initialize()
        project, step = self.app.get_automatic_project_step()

        self.screens[INITIALIZED_SCREEN].set_parameters(self, project, step)
        self.screen_manager.switch_to(self.screens[INITIALIZED_SCREEN])

    def pause(self):
        self.app.pause()

    def calculate_elapsed_time(self, instance=None):
        initialized_datetime = self.screens[INITIALIZED_SCREEN].get_initialized_datetime()
        if datetime.datetime.now() == initialized_datetime:
            return

        hours, remainder = divmod((datetime.datetime.now() - initialized_datetime).seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.screens[INITIALIZED_SCREEN].set_label_elapsed_time(hours, minutes, seconds)
