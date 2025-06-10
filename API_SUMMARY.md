# GitHub API Usage Summary

This document summarizes the GitHub API endpoints, authentication method, and data models used in this project.

## Authentication

-   **Method**: Personal Access Token (PAT) via Bearer Token Authentication.
-   **Header**: `Authorization: Bearer {GITHUB_TOKEN}`
-   **Token Source**: The token is loaded from a `.env` file into the `GITHUB_TOKEN` environment variable.

## API Endpoints

The base URL for all repository-specific API calls is `https://api.github.com/repos/Scytale-exercise/scytale-repo3`.

### 1. List Pull Requests

-   **Endpoint**: `GET /pulls`
-   **Full URL**: `https://api.github.com/repos/Scytale-exercise/scytale-repo3/pulls`
-   **Purpose**: To fetch a list of pull requests from the repository.
-   **Query Parameters**:
    -   `state=closed`: To retrieve only closed PRs.
    -   `per_page=100`: To request up to 100 results per page.
-   **Used in**: `extract.py`

### 2. List Reviews for a Pull Request

-   **Endpoint**: `GET /pulls/{pr_number}/reviews`
-   **Purpose**: To fetch all submitted reviews for a specific pull request to check for an "APPROVED" state.
-   **Used in**: `transform.py` (inside `check_cr_passed` function).

### 3. Get a single Pull Request

-   **Endpoint**: `GET /pulls/{pr_number}`
-   **Purpose**: To get detailed information for a single PR, primarily to find the `head.sha` commit hash.
-   **Used in**: `transform.py` (inside `check_checks_passed` function).

### 4. Get Combined Status for a specific Commit

-   **Endpoint**: `GET /commits/{commit_sha}/status`
-   **Purpose**: To retrieve the combined status of all checks for a specific commit SHA. The overall `state` ("success", "failure", "pending") is checked.
-   **Used in**: `transform.py` (inside `check_checks_passed` function). 