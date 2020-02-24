from .group import Group
from .project import Project
from scipy.interpolate import interp1d


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

    def get_project(self):
        if not self.projects_list:
            return

        priority_mapping_range = interp1d([1, 10],[1, .5])
        sorted_project = sorted(
            [project for project in self.projects_list if not project.finished and
             (project.id != self.current_project.id if self.current_project else True)],
            key=lambda project: project.elapsed_time.seconds * float(priority_mapping_range(project.priority))
        )

        self.current_project = sorted_project[0] if len(sorted_project) > 0 else None
        return self.current_project

    def get_step(self):
        return self.current_project.get_current_step()

    def get_current_project(self):
        return self.current_project

    def validate_step(self):
        #TODO : handle cases where currrent project is None
        self.current_project.validate_step()

    def initialize_groups(self, groups):
        for data_group in groups:
            self.groups_list.append(Group(data_group))

    def initialize_projects(self, projects):
        for data_project in projects:
            self.projects_list.append(Project(data_project))

    def register_elapsed_time(self, elapsed_time):
        self.current_project.register_elapsed_time(elapsed_time)
