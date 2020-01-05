import yaml
import os


from projtimezor.constants import ROOT_DIR


def load_config():
    with open(os.path.join(ROOT_DIR, "config", "default_config.yml")) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)


def get_groups(retrieved_data):
    group_folder_path = os.path.join(ROOT_DIR, "data", "groups")
    group_directory = os.listdir(group_folder_path)
    for group_file_path in group_directory:
        with open(os.path.join(group_folder_path, group_file_path)) as group_file:
            retrieved_data['groups'].append(yaml.load(group_file, Loader=yaml.FullLoader))


def get_projects(retrieved_data):
    project_folder_path = os.path.join(ROOT_DIR, "data", "projects")
    project_directory = os.listdir(project_folder_path)
    for project_file_path in project_directory:
        with open(os.path.join(project_folder_path, project_file_path)) as project_file:
            retrieved_data['projects'].append(yaml.load(project_file, Loader=yaml.FullLoader))


def load_data():
    retrieved_data = {
        'groups': list(),
        'projects': list()
    }
    get_groups(retrieved_data)
    get_projects(retrieved_data)

    return retrieved_data

def save_data(project):
    print(project.json)



