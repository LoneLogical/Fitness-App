# source/dbm/__init__.py

import os

__all__ = ['DB_PATH']

print("Initializing DB Manager")

if not os.path.exists('./db'):
    os.mkdir('./db')

DB_PATH = "./db/fitness.sqlite"

print("Path to DB: " + DB_PATH)
