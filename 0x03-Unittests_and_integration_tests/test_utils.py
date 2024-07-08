#!/usr/bin/env python3
"""Test the utils module"""
from utils import access_nested_map
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function"""

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"a": {"b": {"c": 2}}}, ["a", "b"], {"c": 2}),
        ({"a": {"b": {"c": 4}}}, [], {"a": {"b": {"c": 4}}})
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test the access_nested_map function with exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
