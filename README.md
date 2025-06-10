# GitHub PR Review Checker
### made by - Adi Karif

This project contains scripts to fetch merged pull requests from a specific GitHub repository, check if they passed review and if all status checks were successful, and generate a final report in CSV format.


## Project Structure

- `extract.py`: Fetches raw data of merged pull requests from the GitHub API and saves it to `data/raw_prs.csv`.
- `transform.py`: Reads the raw data, enriches it by checking for approved reviews and successful status checks for each PR, and saves the result to `data/enriched_prs.csv`.
- `config.py`: Handles configuration, including API endpoints and authentication headers.
- `data/`: Directory for output CSV files.
- `requirements.txt`: A list of python packages required to run the project.

---

## Setup and Installation

### Prerequisites
- Python 3.8+
- A GitHub Personal Access Token (PAT) with `repo` scopes.

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root directory of the project and add your GitHub Personal Access Token to it:
    ```
    GITHUB_TOKEN="your_personal_access_token_here"
    ```

---

## How to Run

Execute the scripts in the following order:

1.  **Run the extract script:**
    This will fetch the PR data from GitHub and create `data/raw_prs.csv`.
    ```bash
    python extract.py
    ```

2.  **Run the transform script:**
    This will process the raw data and create the final report `data/enriched_prs.csv`.
    ```bash
    python transform.py
    ```

---

## Output

-   `data/raw_prs.csv`: Intermediate file with the raw pull request data.
-   `data/enriched_prs.csv`: The final report containing the following columns:
    -   `number`: The pull request number.
    -   `title`: The title of the pull request.
    -   `author`: The author of the pull request.
    -   `merged_at`: The timestamp when the PR was merged.
    -   `CR_passed`: (True/False) Whether the PR was approved by at least one reviewer.
    -   `Checks_passed`: (True/False) Whether all required status checks passed before the merge.

## Authentication Method

**Type**: Bearer Token Authentication  
**Header**: `Authorization: Bearer {GITHUB_TOKEN}`  
**Token Source**: Environment variable `GITHUB_TOKEN` (loaded via `.env` file)  
**Additional Headers**: `Accept: application/vnd.github+json`

## Repository Configuration

**Target Repository**: `Scytale-exercise/scytale-repo3`  
**Base URL**: `https://api.github.com/repos/Scytale-exercise/scytale-repo3`

## API Endpoints Used

### 1. Pull Requests List
**Endpoint**: `GET {BASE_URL}/pulls`  
**Purpose**: Fetch closed pull requests  
**Parameters**:
- `state=closed` - Only fetch closed PRs
- `per_page=100` - Return up to 100 results per page

**Usage**: `extract.py` - Initial data extraction of merged PRs

### 2. Pull Request Reviews
**Endpoint**: `GET {BASE_URL}/pulls/{pr_number}/reviews`  
**Purpose**: Get all reviews for a specific pull request  
**Parameters**: None  
**Response**: Array of review objects with `state` field

**Usage**: `transform.py` - Check if PR has approved reviews (`check_cr_passed()`)

### 3. Single Pull Request
**Endpoint**: `GET {BASE_URL}/pulls/{pr_number}`  
**Purpose**: Get detailed information about a specific pull request  
**Parameters**: None  
**Response**: PR object with head SHA information

**Usage**: `transform.py` - Extract commit SHA for status checks (`check_checks_passed()`)

### 4. Commit Status
**Endpoint**: `GET {BASE_URL}/commits/{sha}/status`  
**Purpose**: Get the combined status for a specific commit  
**Parameters**: None  
**Response**: Status object with overall `state` field

**Usage**: `transform.py` - Check if all required checks passed (`check_checks_passed()`)

## Error Handling

- **401 Unauthorized**: Invalid or missing GitHub token
- **403 Forbidden**: Rate limit exceeded or insufficient permissions
- **404 Not Found**: Repository or resource doesn't exist
- **200 Success**: Request completed successfully

## Rate Limits

GitHub API has rate limits:
- **Authenticated requests**: 5,000 requests per hour
- **Search API**: 30 requests per minute

## Required Permissions

The GitHub token needs:
- Repository read access
- Pull request read access
- Status check read access 