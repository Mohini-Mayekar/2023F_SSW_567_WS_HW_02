import requests


#Method invoking GitHub commits API
def gitHubUserCommitDetails(repoList):
    try:
        for repo in repoList:
                REPO = repo['name']
                commits = requests.get("https://api.github.com/repos/"+ID+"/"+REPO+"/commits")
                if(commits.status_code == 200):
                    print("Repo: " + REPO + " Number of commits: " + str(len(commits.json())))
                
        return commits.status_code
    except:
        print("Error - in gitHubUserCommitDetails")
        return 0

#Method invoking GitHub repo list API
def gitHubUserRepoDetails(ID):
    try:
        response = requests.get("https://api.github.com/users/"+ID+"/repos")
        statusCode = 0
        print("Status code: ", response.status_code)
        if(response.status_code == 200):
            repoList = response.json()

            print(len(repoList))

            if(len(repoList) > 0):
                statusCode = gitHubUserCommitDetails(repoList)                
            else:
                print("No repositories present")
        return 0 if (statusCode != 200) else statusCode
    except:
        print("Error - in gitHubUserRepoDetails")
        return 0

if __name__ == '__main__':
    #Input from the user - user ID
    ID = input('Please enter GitHub User ID: ' )

    print("User ID: " + ID)

    gitHubUserRepoDetails(ID)
    
