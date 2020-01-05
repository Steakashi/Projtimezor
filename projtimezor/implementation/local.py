import yaml
import os
import json


from projtimezor.constants import ROOT_DIR, GROUP_FOLDER_PATH, PROJECT_FOLDER_PATH


def load_config():
    with open(os.path.join(ROOT_DIR, "config", "default_config.yml")) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)


def get_groups(retrieved_data):
    group_directory = os.listdir(GROUP_FOLDER_PATH)
    for group_file_path in group_directory:
        with open(os.path.join(GROUP_FOLDER_PATH, group_file_path)) as group_file:
            loaded_group = yaml.load(group_file, Loader=yaml.FullLoader)
            loaded_group['filename'] = group_file_path
            retrieved_data['groups'].append(loaded_group)


def get_projects(retrieved_data):
    project_directory = os.listdir(PROJECT_FOLDER_PATH)
    for project_file_path in project_directory:
        with open(os.path.join(PROJECT_FOLDER_PATH, project_file_path)) as project_file:
            loaded_project = json.load(project_file)
            loaded_project['filename'] = project_file_path
            retrieved_data['projects'].append(loaded_project)


def load_data():
    retrieved_data = {
        'groups': list(),
        'projects': list()
    }
    get_groups(retrieved_data)
    get_projects(retrieved_data)

    return retrieved_data


def save_data(project):
    with open(os.path.join(PROJECT_FOLDER_PATH, project.filename), 'w') as project_file:
        json.dump(project.json, project_file, indent=4)

