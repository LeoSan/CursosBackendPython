import os

DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "notes.sqlite")


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False