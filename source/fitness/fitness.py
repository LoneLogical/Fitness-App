# source/fitness/fitness.py

import pickle
from . import PK_PATH
import os


class Exercise:
    """
    Exercise class
    """

    def __init__(self, name, fields=None):
        self.name = name
        if fields is not None:
            self.fields = fields
        else:
            self.fields = {}

    def add_field(self, f_name, f_type):
        """
        add_field function creates attribute for particular exerise to be stored in database. Function assumes
        f_type is a proper data type for sqlite db because user won't type in this field. Will be preselected on gui.
        :param f_name: (String) Name of attribute field
        :param f_type: (String) Name of data type for interfacing with sqlite database
        :return:
        """
        if f_name in self.fields:
            print("Error in add field")
            return
        self.fields[f_name] = f_type
        return


class Fitness:
    """
    Fitness Class Holds all user's exercise instances
    """

    def __init__(self):
        self.exercises = {}

    def add_exercise(self, name, fields):
        """
        Add new exercise to fitness class
        :param name: String - name of the exercise
        :param fields: Dict of data that needs to be stored for this exercise
        :return:
        """
        if name in self.exercises:
            print("ERROR: exercise already exists")
        else:
            self.exercises[name] = Exercise(name=name, fields=fields)

    def print_fitness_plan(self):
        """
        Check functionality of Fitness and Exercise class
        :return:
        """
        print("Printing Fitness Plan")
        for ex_name, ex_obj in self.exercises.items():
            print("Exercise: " + ex_name)
            for f_name, f_type in ex_obj.fields.items():
                print("    " + f_name + " : " + f_type)

    def save_session(self):
        """
        Use Pickle to save exercise instances to a file for use next time program boots up
        :return:
        """
        exer_dict = {}

        for ex_name, ex_obj in self.exercises.items():
            exer_dict[ex_name] = ex_obj.fields

        outfile = open(PK_PATH, 'wb')
        pickle.dump(exer_dict, outfile)
        outfile.close()

    def open_session(self):
        """
        Use pickle to resume application save state if there was one. Otherwise use fresh start.
        :return: True if already existed save state. False if otherwise
        """
        if not os.path.exists(PK_PATH):
            return False

        infile = open(PK_PATH, 'rb')
        exer_dict = pickle.load(infile)
        infile.close()

        for ex_name, ex_fields in exer_dict.items():
            self.exercises[ex_name] = Exercise(name=ex_name, fields=ex_fields)

        return True
