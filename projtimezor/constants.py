from pathlib import Path
import os


ROOT_DIR = Path(__file__).parent.parent
#ROOT_DIR = "D:\Projtimezor"
PROJECT_FOLDER_PATH = os.path.join(ROOT_DIR, "data", "projects")
GROUP_FOLDER_PATH = os.path.join(ROOT_DIR, "data", "groups")

START_SCREEN = 'start_screen'
INITIALIZED_SCREEN = 'initialized_screen'
PROJECT_CREATION_SCREEN = 'project_creation_screen'

STATE_FINISHED = 'finished'