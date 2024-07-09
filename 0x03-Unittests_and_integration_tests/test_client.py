#!/usr/bin/env python3
"""Test the client module"""
from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": False})
    ])
    @patch('client.get_json')
    def test_org(self, test_org, test_payload, mock_get):
        """Test org"""
        mock_get.return_value = test_payload
        org = GithubOrgClient(test_org)

        self.assertEqual(org.org, test_payload)
        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{test_org}'
        )


if __name__ == "__main__":
    unittest.main()
