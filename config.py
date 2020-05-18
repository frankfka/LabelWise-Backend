import configparser
import os
import pathlib

"""
Global store of configuration for the project. It's important that this is in the root
"""

root_project_path = pathlib.Path(__file__).parent.absolute()

# Get app config object
config = configparser.ConfigParser()
config.read(os.path.join(root_project_path, "config.ini"))
appConfig = config["APP"]

# Get attrs from our app config
vision_credentials_path = os.path.join(root_project_path, appConfig["VisionCredentialsPath"])
ingredients_db_path = os.path.join(root_project_path, appConfig["IngredientDatabasePath"])
api_key = appConfig["ApiKey"]


class AppConfig:
    class WrappedAppConfig:

        def __init__(self):
            self.vision_cred_filepath = vision_credentials_path
            self.ingredients_db_dirpath = ingredients_db_path
            self.api_key = api_key

    __instance = None  # Singleton instance

    def __init__(self):
        if not AppConfig.__instance:
            AppConfig.__instance = AppConfig.WrappedAppConfig()

    def __getattr__(self, name):
        return getattr(self.__instance, name)


class AppTestConfig:

    def __init__(self):
        self.vision_cred_filepath = vision_credentials_path
        self.ingredients_db_dirpath = ingredients_db_path
        self.test_assets_dir = os.path.join(root_project_path, "test_assets")
