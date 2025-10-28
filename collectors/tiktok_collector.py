from TikTokApi import TikTokApi
def fetch_tiktok(hashtag="osint", count=10):
    results = []
    with TikTokApi() as api:
        for v in api.hashtag(name=hashtag).videos(count=count):
            results.append({
                "platform": "tiktok",
                "user": v.author.username,
                "timestamp": str(v.create_time),
                "text": v.desc,
                "url": f"https://www.tiktok.com/@{v.author.username}/video/{v.id}"
            })
    return results