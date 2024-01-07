#!/usr/bin/python3
"""logical"""
import requests
from sys import argv

if __name__ == "__main__":
    rq = requests.get("https://api.github.com/repos/rails/rails/commits",
                      params={'sort': 'committer-date-asc'},
                      auth=(argv[1], argv[2]))

    for _ in rq.json()[:10]:
        print(_.get("commit").get("tree").get("sha"), end=": ")
        print(_.get("commit").get("author").get("name"), end="\n\n")
