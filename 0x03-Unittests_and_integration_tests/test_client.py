#!/usr/bin/env python3
"""Test the client module"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """Test the org method of GithubOrgClient"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get.called_once_with(test_class.ORG_URL.format(org=org_name))


if __name__ == "__main__":
    unittest.main()
