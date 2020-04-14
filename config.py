# TODO: export hard coded config into a yaml file

"""
Global store of configuration for the project. It's important that this is in the root
"""
import os
import pathlib

__REL_PATH_CREDS = "assets/credentials.json"
__REL_PATH_INGREDIENTS_DB = "assets/ingredients_db"

__PROJ_PATH = pathlib.Path(__file__).parent.absolute()

# Exported
VISION_CREDIENTIALS_FILEPATH = os.path.join(__PROJ_PATH, __REL_PATH_CREDS)
INGREDIENTS_DB_FILEPATH = os.path.join(__PROJ_PATH, __REL_PATH_INGREDIENTS_DB)