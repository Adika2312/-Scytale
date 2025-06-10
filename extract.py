import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "Scytale-exercise/scytale-repo3"
BASE_URL = f"https://api.github.com/repos/{REPO}/pulls"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}











