import logging
from difflib import SequenceMatcher

ONTOLOGY_MAP = {
    "delayed": "Delivery issue",
    "delay": "Delivery issue",
    "delivery": "Delivery issue",
    "rude": "Delivery partner rude",
    "badly": "Delivery partner rude",
    "impolite": "Delivery partner rude",
    "stale": "Food stale",
    "spoiled": "Food stale",
    "maps": "Maps not working properly",
    "navigation": "Maps not working properly",
    "map not": "Maps not working properly",
    "bolt": "Bolt delivery request",
    "10 minute": "Bolt delivery request",
    "24/7": "All-night service request",
    "24 hours": "All-night service request",
    "24": "All-night service request",
    "instamart": "All-night service request",
    "support": "Customer support issue",
    "payment": "Payment/App crash issue",
    "froze": "Payment/App crash issue",
    "crash": "Payment/App crash issue",
    "crashes": "Payment/App crash issue",
    "ui": "UI/UX feedback",
    "layout": "UI/UX feedback",
    "interface": "UI/UX feedback",
    "bad": "UI/UX feedback"
}

def match_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def extract_topics(reviews):
    """Extract topics with high recall using ontology rules"""
    topics = []
    for review in reviews:
        r = review.lower()
        matched = False
        for key, topic in ONTOLOGY_MAP.items():
            if key in r:
                topics.append(topic)
                matched = True
                break
        if not matched:
            topics.append("New:" + review[:20])
    return topics

def consolidate_topics(topics):
    """Merge similar topics to avoid fragmentation"""
    canonical = []
    for t in topics:
        if not any(match_similarity(t, c) > 0.84 for c in canonical):
            canonical.append(t)
    logging.info(f"Consolidated into {len(canonical)} topics")
    return canonical
