from pathlib import Path
import os


ROOT_DIR = Path(__file__).parent.parent
PROJECT_FOLDER_PATH = os.path.join(ROOT_DIR, "data", "projects")
GROUP_FOLDER_PATH = os.path.join(ROOT_DIR, "data", "groups")

START_SCREEN = 'start_screen'
INITIALIZED_SCREEN = 'initialized_screen'
