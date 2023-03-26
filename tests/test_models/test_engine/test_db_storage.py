#!/usr/bin/python3
import unittest
from models.state import State
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip when the storage is not db")
class TestDBStorage(unittest.TestCase):
        """db storage tests"""

        def test_state(self):
            """ test state table"""
            state = State(name="test")
            state.save()
            self.assertTrue(state.id in self.storage.all())
            self.assertEqual(state.name, "test")
