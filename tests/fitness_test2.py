# tests/fitness_test2.py

import source.fitness.fitness as fit
import os

fit_app = fit.Fitness()

test1 = fit_app.open_session()
if not test1:
    print("ERROR: session should exist")
else:
    print("Test1 passed")

fit_app.print_fitness_plan()

fit_app.save_session()

test2 = os.path.exists('./pickles/exercises.pk')
if test2:
    print("test2 passed")
else:
    print("ERROR: session was not saved")