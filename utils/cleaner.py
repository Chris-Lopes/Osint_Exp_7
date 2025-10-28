import re
from langdetect import detect
def clean_text(text):
    text = re.sub(r"http\S+", "", text) # remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text) # remove symbols
    return text.strip()
def filter_english(records):    
    return [r for r in records if detect(r["text"]) == "en"]