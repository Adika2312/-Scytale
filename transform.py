import pandas as pd
from dotenv import load_dotenv
import os
import requests


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "Scytale-exercise/scytale-repo3"
BASE_URL = f"https://api.github.com/repos/{REPO}"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

df = pd.read_csv("data/raw_prs.csv")

def get_cr_passed(pr_number):
    url = f"{BASE_URL}/pulls/{pr_number}/reviews"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        reviews = resp.json()
        for review in reviews:
            if review.get("state") == "APPROVED":
                return True
    return False


