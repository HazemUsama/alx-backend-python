#!/usr/bin/env python3
"""Test the client module"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock


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

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {'repos_url': 'data'}
            mock.return_value = payload

            test_class = GithubOrgClient('corp')
            result = test_class._public_repos_url
            self.assertEqual(result, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """Test the public_repos method"""
        payload = [{'name': 'google'}, {'name': 'facebook'}]
        mock_get.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url') as mock_repo:
            mock_repo.return_value = 'Any thing!'
            test_class = GithubOrgClient('corp')
            result = test_class.public_repos()

            expected = [repo["name"] for repo in payload]
            self.assertEqual(expected, result)
            mock_get.called_with_once()
            mock_repo.called_with_once()


if __name__ == "__main__":
    unittest.main()
