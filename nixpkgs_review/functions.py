import json
import os
import subprocess

from github import Github
from jq import jq
import requests
here = os.path.abspath(os.path.dirname(__file__))

def ghtoken():
    token = os.getenv('GITHUB_TOKEN')
    return token

def ghapi(request, PR="", text=""):
    g = Github(ghtoken())
    repo = g.get_repo("NixOS/nixpkgs")
    pr = repo.get_pull(PR)
    if request == "myuser":
         return g.get_user().login
    elif request == "pruser":
        return pr.user.login
    elif request == "prstatus":
        return pr.state
    elif request == "gist":
        text = "hi"
        

def tb(input):
    text = subprocess.run(["tail", "-20000"], text=True, input=input, stdout=subprocess.PIPE)
    subprocess.run(["nc", "termbin.com", "9999"], text=True, input=text.stdout)


def ofborg_state(PR):
    text = '''query Query ($PR: Int!) {
  repository(name: "nixpkgs", owner: "NixOS") {
    pullRequest(number: $PR) {
      commits(last: 1) {
        nodes {
          commit {
            checkSuites(last: 1) {
              nodes {
                checkRuns(filterBy: {checkType: LATEST, appId: 20500}, last: 10) {
                  nodes {
                    url
                    title
                    summary
                    name
                    detailsUrl
                    conclusion
                    checkSuite {
                      app {
                        slug
                        databaseId
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}'''

    url = "https://api.github.com/graphql"
    headers = {'Authorization': f"token {ghtoken()}"}
    variables = {"PR": int(PR)}
    r = requests.post(url, headers=headers, json={"query": text, "variables": variables}).text
    
    arch = subprocess.check_output(["nix-instantiate", "--eval", "--json", "--expr", "builtins.currentSystem"], text=True).replace('"', '')
    status = jq(f".[][][][][][][][][][][][][]|select(.name | contains(\"passthru.tests on {arch}\")).conclusion").transform(json.loads(r))
    return status




