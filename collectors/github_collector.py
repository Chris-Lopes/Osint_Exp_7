from github import Github
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def fetch_github(query="leak", limit=10):
    """Search GitHub repositories and return a list of results.

    Uses the GITHUB_TOKEN environment variable (loaded from `.env` if present).
    If no token is found, an unauthenticated client is used (may be rate-limited).
    """
    token = os.getenv("GITHUB_TOKEN")
    if token:
        g = Github(token)
    else:
        logger.warning("GITHUB_TOKEN not found in environment; using unauthenticated Github client which may be rate-limited.")
        g = Github()

    repos = g.search_repositories(query=query)
    results = []
    for repo in repos[:limit]:
        results.append({
            "platform": "github",
            "user": repo.owner.login,
            "timestamp": str(repo.created_at),
            "text": repo.description or "",
            "url": repo.html_url
        })
    return results