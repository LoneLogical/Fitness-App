# source/exercise/__init__.py

import os

if not os.path.exists('./pickles'):
    os.mkdir('./pickles')

PK_PATH = "./pickles/exercises.pk"
