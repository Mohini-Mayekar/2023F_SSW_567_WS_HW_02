import unittest
import requests
import json

from GitHubApi import gitHubUserCommitDetails, gitHubUserRepoDetails

class TestGitHubApi(unittest.TestCase):

 #   file = open('RepoList.json')
 #   data = json.loads(file)

    def test_HappyPath(self):
        repoDetails = gitHubUserRepoDetails('Mohini-Mayekar')
        self.assertEqual(repoDetails, 200, "Success")

   # def test_HappyPath2(self, data):
   #     repoDetails = gitHubUserCommitDetails(data)
   #     self.assertEqual(repoDetails, "200", "Success")

    def test_url_repo(self):
        repoUrl = "https://api.github.com/users/Mohini-Mayekar/repos"
        response = requests.get(repoUrl)
        assert response.status_code == 200

    def test_url_commit(self):
        commitUrl = "https://api.github.com/repos/Mohini-Mayekar/2023F_SSW_567_WS_HW_01/commits"
        response = requests.get(commitUrl)
        assert response.status_code == 200

 #   def test_Forbidden_or_tooManyRequest(self):
 #       repoDetails = gitHubUserRepoDetails('Mohini-Mayekar')
 #       self.assertEqual(repoDetails, 0, "403")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
