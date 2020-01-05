from projtimezorui.main_window import MainWindow
from .implementation import default, local
from .model.manager import Manager


import datetime


class MainApp:

    provider = default
    manager = None
    config = None
    processing = False
    session_elapsed_time = datetime.timedelta()

    def __init__(self):
        self.set_implementation()
        self.set_config()
        main_window = MainWindow(self)
        main_window.run()

    def set_implementation(self):
        self.provider = local

    def set_config(self):
        self.config = self.provider.load_config()

    def get_data(self):
        return self.provider.load_data()

    def get_automatic_project_step(self):
        project = self.manager.get_automatic_project()
        step = project.get_current_step()
        return project, step

    def initialize(self):
        self.manager = Manager(self.get_data())

    def is_processing(self):
        return self.processing

    def pause(self):
        self.processing = False

    def resume(self):
        self.processing = True

    def save(self):
        self.provider.save_data(self.manager.get_current_project())

    def register_elapsed_time(self, elapsed_time):
        self.manager.register_elapsed_time(elapsed_time)
        self.session_elapsed_time += elapsed_time
        return self.session_elapsed_time
