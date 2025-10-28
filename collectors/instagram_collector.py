import instaloader
L = instaloader.Instaloader()
def fetch_instagram(username="bbcnews", limit=5):
    profile = instaloader.Profile.from_username(L.context, username)
    results = []
    for i, post in enumerate(profile.get_posts()):
        if i >= limit: break
        results.append({
            "platform": "instagram",
            "user": username,
            "timestamp": str(post.date),
            "text": post.caption,
            "url": post.url
        })
    return results