import re
from langdetect import detect, LangDetectException

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"http\S+", "", text) # remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text) # remove symbols
    return text.strip()

def filter_english(records):
    """Filter records to keep only English text.
    
    Skips records with empty text or text that can't be detected.
    """
    english_records = []
    for r in records:
        try:
            if r.get("text") and r["text"].strip() and detect(r["text"]) == "en":
                english_records.append(r)
        except LangDetectException:
            # Skip records where language can't be detected (empty, too short, etc.)
            pass
    return english_records