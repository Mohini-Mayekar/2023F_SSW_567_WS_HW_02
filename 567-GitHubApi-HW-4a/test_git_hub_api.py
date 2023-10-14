"""Module containing test cases for invoking GitHub APIs"""

import unittest
import os
import json
import sys
from unittest.mock import Mock, patch
import requests
from git_hub_api import git_hub_user_commit_details, git_hub_user_repo_details
from constants import REPO_URL, COMMIT_URL, USER_ID, TIMEOUT, FILE_PATH

sys.path.append('./567-GitHubApi-HW-4a')
sys.path.append('./567-GitHubApi-HW-4a/test-results')

class TestGitHubApi(unittest.TestCase):
    """Test cases for git_hub_api"""



    def load_data(self):
        """Function to load data from json file"""
        path = os.path.abspath("567-GitHubApi-HW-4a/repo_list.json")
        
        with open(path, mode="r", encoding="utf8") as file:
            json_data = file.read()
        data = json.loads(json_data)
        return data

    def test_git_hub_user_repo_details(self):
        """Invoke git_hub_user_repo_details function"""
        repo_details = git_hub_user_repo_details(USER_ID)
        self.assertEqual(repo_details, 200, "Success")

    def test_git_hub_user_commit_details(self):
        """Invoke git_hub_user_commit_details function"""
        data = TestGitHubApi.load_data(self)

        commit_details = git_hub_user_commit_details(USER_ID, data)
        self.assertEqual(commit_details, 200, "Success")

    def test_url_repo(self):
        """Directly invoking GitHub API to get repositor list of for an user"""
        response = requests.get(REPO_URL, timeout= TIMEOUT)
        assert response.status_code == 200

    def test_url_commit(self):
        """Directly invoking GitHub API to get repositor list of for an user"""
        response = requests.get(COMMIT_URL, timeout= TIMEOUT)
        assert response.status_code == 200


    @patch("git_hub_api.requests.get")
    def test_git_hub_user_repo_details_ok(self, mock_get):
        """Invoke git_hub_user_repo_details function"""
        mock_get.return_value.ok = True
        repo_details = git_hub_user_repo_details(USER_ID)
        self.assertIsNotNone(repo_details)

    @patch("git_hub_api.requests.get")
    def test_git_hub_user_repo_details_not_ok(self, mock_get):
        """Invoke git_hub_user_repo_details function"""
        mock_get.return_value.ok = False
        repo_details = git_hub_user_repo_details(USER_ID)
        self.assertIs(repo_details, 0)

    @patch("git_hub_api.requests.get")
    def test_git_hub_user_commit_details_ok(self, mock_get):
        """Invoke git_hub_user_commit_details function"""
        data = TestGitHubApi.load_data(self)
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = data
        commit_details = git_hub_user_commit_details(USER_ID, data)
        self.assertIsNotNone(commit_details)

    @patch("git_hub_api.requests.get")
    def test_git_hub_user_commit_details_not_ok(self, mock_get):
        """Invoke git_hub_user_commit_details function""" 
        data = TestGitHubApi.load_data(self)
        mock_get.return_value.ok = False
        mock_get.return_value.json.return_value = data
        commit_details = git_hub_user_commit_details(USER_ID, data)
        self.assertIs(commit_details, 0)

if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
