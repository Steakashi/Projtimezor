from .group import Group
from .project import Project


class Manager:

    def __init__(self, data):
        self.groups_list = list()
        self.projects_list = list()
        self.initialize_groups(data['groups'])
        self.initialize_projects(data['projects'])
        self.current_project = None

    @property
    def groups(self):
        return [group.properties for group in self.groups_list]

    @property
    def projects(self):
        return [project.properties for project in self.projects_list]

    def get_automatic_project(self):
        if not self.projects_list:
            return

        self.current_project = sorted(self.projects_list, key=lambda project: project.elapsed_time)[0]
        return self.current_project

    def get_current_project(self):
        return self.current_project

    def initialize_groups(self, groups):
        for data_group in groups:
            self.groups_list.append(Group(data_group))

    def initialize_projects(self, projects):
        for data_project in projects:
            self.projects_list.append(Project(data_project))

    def register_elapsed_time(self, elapsed_time):
        return self.current_project.register_elapsed_time(elapsed_time)
