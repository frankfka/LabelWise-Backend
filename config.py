# TODO: export hard coded config into a yaml file

"""
Global store of configuration for the project. It's important that this is in the root
"""
import os
import pathlib

REL_PATH_CREDS = "assets/credentials.json"
REL_PATH_INGREDIENTS_DB = "assets/ingredients_db"

PROJ_PATH = pathlib.Path(__file__).parent.absolute()


class AppConfig:

    def __init__(self):
        # TODO: we can init using a hard coded config file
        self.vision_cred_filepath = os.path.join(PROJ_PATH, REL_PATH_CREDS)
        self.ingredients_db_dirpath = os.path.join(PROJ_PATH, REL_PATH_INGREDIENTS_DB)


class AppTestConfig:

    def __init__(self):
        self.vision_cred_filepath = os.path.join(PROJ_PATH, REL_PATH_CREDS)
        self.ingredients_db_dirpath = os.path.join(PROJ_PATH, REL_PATH_INGREDIENTS_DB)
        self.test_assets_dir = os.path.join(PROJ_PATH, "test_assets")
