import os
import requests
import pandas as pd
from dotenv import load_dotenv
from config import PULLS_URL, headers

#send the request
params = {
    "state": "closed",
    "per_page": 100
}

response = requests.get(PULLS_URL, headers=headers, params=params)

#check if the request was successful
if response.status_code == 200:
    pull_requests = response.json()
    merged_pull_requests = [pr for pr in pull_requests if pr.get("merged_at")]

    print(f"Found {len(merged_pull_requests)} merged PRs")

    #create csv
    pr_data = [
        {
        "number":pr.get("number"),
        "title":pr.get("title"),
        "author":pr.get("user").get("login"),
        "merged_at":pr.get("merged_at"),
        "CR_passed": None,
        "Checks_passed": None
        }
        for pr in merged_pull_requests
    ]

    df = pd.DataFrame(pr_data)
    df.to_csv("data/raw_prs.csv", index=False)

    print("Saved to data/raw_prs.csv")

else:
    print("Failed to fetch PRs:", response.status_code, response.text)










