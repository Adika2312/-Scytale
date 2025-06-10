import pandas as pd
from dotenv import load_dotenv
import os
import requests
from config import BASE_URL, headers


df = pd.read_csv("data/raw_prs.csv")

def check_cr_passed(pr_number):

    """return True if the pr passed code review, False otherwise"""

    url = f"{BASE_URL}/pulls/{pr_number}/reviews"
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        reviews = resp.json()

        for review in reviews:

            if review.get("state") == "APPROVED":
                return True
            
    else:
        print(f"Failed to fetch reviews for PR #{pr_number}")
        return False
    

def check_checks_passed(pr_number):

    """return True if all the required checks are passed, False otherwise"""

    pr_url = f"{BASE_URL}/pulls/{pr_number}"
    pr_resp = requests.get(pr_url, headers=headers)

    if pr_resp.status_code != 200:
        print(f"Failed to fetch PR #{pr_number}")
        return None
    
    pr_data = pr_resp.json()
    sha = pr_data.get("head", {}).get("sha")

    if not sha:
        return None
    
    status_url = f"{BASE_URL}/commits/{sha}/status"
    status_resp = requests.get(status_url, headers=headers)

    if status_resp.status_code != 200:
        print(f"Failed to fetch status for SHA {sha}")
        return None
    
    status_data = status_resp.json()
    return status_data.get("state") == "success"


#check if the pr passed code review and all the required checks are passed
for index, row in df.iterrows():
    pr_number = row["number"]
    df.at[index, "CR_passed"] = check_cr_passed(pr_number)
    df.at[index, "Checks_passed"] = check_checks_passed(pr_number)
    
#save the enriched prs to a csv file
df.to_csv("data/enriched_prs.csv", index=False)
print("Saved enriched PRs to data/enriched_prs.csv ✅")


