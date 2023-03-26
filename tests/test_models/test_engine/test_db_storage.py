#!/usr/bin/python3
import unittest
from models.state import State
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
class TestDBStorage(unittest.TestCase):
        def test_state(self):
            """ test state table"""
            state = State(name="test")
            state.save()
            self.assertTrue(state.id in self.storage.all())
            self.assertEqual(state.name, "test")