"""Module invoking GitHub APIs"""

import requests

from constants import TIMEOUT


# Method invoking GitHub commits API
def git_hub_user_commit_details(user_id, repo_list):
    """Function invoking GitHub API to get the commit details of a repository for an user"""
    try:
        for repo in repo_list:
            repo = repo["name"]
            commits = requests.get(
                "https://api.github.com/repos/" + user_id + "/" + repo + "/commits",
                timeout=TIMEOUT,
            )
            if commits.status_code == 200:
                print(
                    "Repo: " + repo + " Number of commits: " + str(len(commits.json()))
                )

        return 0 if (commits.status_code != 200) else commits.status_code
    except TimeoutError:
        print("TimeoutError - in git_hub_user_commit_details")
    except requests.exceptions.HTTPError:
        print("HTTPError - in git_hub_user_commit_details")
    #except:
    #    print("Error - in git_hub_user_commit_details")
    #   return 0


# Method invoking GitHub repo list API
def git_hub_user_repo_details(user_id):
    """Function invoking GitHub API to get the repository details of an user"""
    try:
        response = requests.get(
            "https://api.github.com/users/" + user_id + "/repos", timeout=TIMEOUT
        )
        status_code = 0
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            repo_list = response.json()

            print(len(repo_list))

            if len(repo_list) > 0:
                status_code = git_hub_user_commit_details(user_id, repo_list)
            else:
                print("No repositories present")
        return 0 if (status_code != 200) else status_code
    except TimeoutError:
        print("TimeoutError - in git_hub_user_repo_details")
    except requests.exceptions.HTTPError:
        print("HTTPError - in git_hub_user_repo_details")
    #except:
    #    print("Error - in git_hub_user_repo_details")
    #    return 0


if __name__ == "__main__":
    # Input from the user - user ID
    ip_user_id = input("Please enter GitHub User ID: ")

    print("User ID: " + ip_user_id)

    git_hub_user_repo_details(ip_user_id)
