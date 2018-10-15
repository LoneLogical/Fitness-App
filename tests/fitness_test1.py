# tests/fitness_test1.py

import source.fitness.fitness as fit
import os

fit_app = fit.Fitness()

test1 = fit_app.open_session()
if test1:
    print("ERROR: session should not exist")
else:
    print("Test1 passed")

run_fields = {'date': 'DATE', 'distance': 'FLOAT', 'time': 'INTEGER'}
fit_app.add_exercise('Running', run_fields)

fit_app.print_fitness_plan()

fit_app.save_session()

test2 = os.path.exists('./pickles/exercises.pk')
if test2:
    print("test2 passed")
else:
    print("ERROR: session was not saved")
