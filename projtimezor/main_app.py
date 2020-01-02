from projtimezorui.main_window import MainWindow
from .implementation import default, local
from .model.manager import Manager


class MainApp:

    provider = default
    manager = None

    def __init__(self):
        self.set_implementation()
        self.set_config()
        main_window = MainWindow(self)
        main_window.run()

    def initialize(self):
        self.manager = Manager(self.get_data())

    def pause(self):
        pass

    def set_implementation(self):
        self.provider = local

    def set_config(self):
        self.provider.load_config()

    def get_data(self):
        return self.provider.load_data()

    def get_automatic_project_step(self):
        project = self.manager.get_automatic_project()
        step = project.get_current_step()
        return project, step
