# tests/db_test.py

import source.dbm.dbmanager as dbma

fa_db = dbma.DBManager()
fa_db.create_table()
fa_db.query()
fa_db.close()





