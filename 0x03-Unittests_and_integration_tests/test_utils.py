#!/usr/bin/env python3
"""Parametize a unit test"""
import unittest


from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ tests the function for following inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, resultc):
        """ method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), result)
