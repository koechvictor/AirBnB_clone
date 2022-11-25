#!/usr/bin/python3
""" creates a unique Filestorage instance for application """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
