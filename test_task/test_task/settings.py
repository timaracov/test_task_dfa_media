import os
import pathlib


class AppSettings:
    ROOT_PATH = pathlib.Path(__name__).parents[0].absolute()

    DB_FILENAME = "db.sqlite"
    DB_URI = "sqlite:///" + os.path.join(ROOT_PATH, DB_FILENAME)
