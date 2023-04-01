"""
__init__.py is a special python file that is
used to mark a directory as a python package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()