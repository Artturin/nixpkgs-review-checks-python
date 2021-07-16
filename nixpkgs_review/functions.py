import subprocess
import os
import requests
from pprint import pprint
from jq import jq
import json
here = os.path.abspath(os.path.dirname(__file__))

def test_func(name):
    print("hi " + name)

def ghtoken():
    token = os.getenv('GITHUB_TOKEN')
    print(token)
    return token

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
    print(jq(f".[][][][][][][][][][][][][]|select(.name | contains(\"passthru.tests on {arch}\")).conclusion").transform(json.loads(r)))




