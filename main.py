import sys
import urllib.request
import json

if __name__ == "__main__":
    repo = sys.argv[1]  # owner/repo format
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"User-Agent": "repo-stats"}
    )
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    print(f"repo: {data['full_name']}")
    print(f"stars: {data['stargazers_count']}")
    print(f"forks: {data['forks_count']}")
    print(f"issues: {data['open_issues_count']}")
    print(f"language: {data.get('language')}")
    print(f"created: {data['created_at'][:10]}")
