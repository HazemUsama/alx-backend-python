#!/usr/bin/env python3
"""Test the utils module"""
from utils import access_nested_map, get_json
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """Test the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test the get_json function"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
