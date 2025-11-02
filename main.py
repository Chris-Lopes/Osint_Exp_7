# from collectors.twitter_collector import fetch_twitter
from collectors.reddit_collector import fetch_reddit
# from collectors.facebook_collector import fetch_facebook
from collectors.instagram_collector import fetch_instagram
from collectors.github_collector import fetch_github
from utils.cleaner import clean_text, filter_english
from utils.database import save_to_db
from utils.sentiment import add_sentiment
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Collect
data = []

# Helper function to safely collect data
def safe_collect(collector_func, platform_name, *args, **kwargs):
    """Attempt to collect data from a platform, handling errors gracefully."""
    try:
        logger.info(f"Collecting from {platform_name}...")
        results = collector_func(*args, **kwargs)
        logger.info(f"✓ Collected {len(results)} records from {platform_name}")
        return results
    except Exception as e:
        logger.error(f"✗ Failed to collect from {platform_name}: {type(e).__name__}: {e}")
        return []

# data.extend(safe_collect(fetch_twitter, "Twitter", "AI", 10))
data.extend(safe_collect(fetch_reddit, "Reddit", "crypto", 10))
data.extend(safe_collect(fetch_github, "GitHub", "ai", 10))
# data.extend(safe_collect(fetch_facebook, "Facebook", "cnn", 5))
data.extend(safe_collect(fetch_instagram, "Instagram", "nasa", 5))

# Clean
for d in data:
    d["text"] = clean_text(d["text"])
data = filter_english(data)
# Enrich
data = add_sentiment(data)
# Store
save_to_db(data)
print(f"Collected and stored {len(data)} OSINT records.")