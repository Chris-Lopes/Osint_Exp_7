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




# import instaloader
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def fetch_instagram(username="bbcnews", limit=5):
#     """Fetch Instagram posts. Requires login for reliable access.
    
#     Set INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD in .env file, or
#     run this once interactively to save session:
#         from instaloader import Instaloader
#         L = Instaloader()
#         L.login("your_username", "your_password")
#         L.save_session_to_file()
#     """
#     L = instaloader.Instaloader()
    
#     # Try to load saved session first
#     instagram_user = os.getenv("INSTAGRAM_USERNAME")
    
#     if instagram_user:
#         try:
#             # Try loading session from file
#             L.load_session_from_file(instagram_user)
#         except FileNotFoundError:
#             # If no session file, try to login with password
#             instagram_pass = os.getenv("INSTAGRAM_PASSWORD")
#             if instagram_pass:
#                 L.login(instagram_user, instagram_pass)
#                 # Optionally save session for future use
#                 # L.save_session_to_file()
#             else:
#                 raise ValueError("INSTAGRAM_PASSWORD not found in environment")
    
#     profile = instaloader.Profile.from_username(L.context, username)
#     results = []
#     for i, post in enumerate(profile.get_posts()):
#         if i >= limit: break
#         results.append({
#             "platform": "instagram",
#             "user": username,
#             "timestamp": str(post.date),
#             "text": post.caption or "",
#             "url": post.url
#         })
#     return results