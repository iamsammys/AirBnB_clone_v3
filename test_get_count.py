#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

palales = ""
print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(palales)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(palales, first_state_id)))
