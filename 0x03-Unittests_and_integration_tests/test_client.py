#!/usr/bin/env python3
"""Test the client module"""
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock, PropertyMock
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, test_repo, license_key, expected):
        """Test the has_license method"""
        test_class = GithubOrgClient('corp')
        self.assertEqual(
            test_class.has_license(test_repo, license_key), expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class with integration test"""
    @classmethod
    def setUp(cls):
        """Setup the test"""
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.repos_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDown(cls):
        """Teardown the test"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method"""
        test_class = GithubOrgClient('google')
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Test the public_repos method with license"""
        test_class = GithubOrgClient('google')
        self.assertEqual(
            test_class.public_repos("apache-2.0"), self.apache2_repos
        )
        self.mock_get.assert_called()


if __name__ == "__main__":
    unittest.main()
