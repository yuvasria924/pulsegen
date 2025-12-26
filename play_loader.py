import random
from datetime import datetime, timedelta
import logging, os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

REVIEW_POOL = [
    "Delivery was delayed today",
    "Delivery partner was rude",
    "Delivery person behaved badly",
    "Food is stale and spoiled",
    "Food arrived spoiled",
    "Maps not loading properly",
    "Map navigation is broken",
    "Need 10 minute bolt delivery again",
    "Bring back bolt delivery",
    "Instamart should be open 24/7",
    "Customer support not responding",
    "App crashes during payment",
    "Payment failed and app froze",
    "UI layout is confusing",
    "App interface is bad"
]

def load_daily_batches(start="2024-06-01"):
    """Simulate daily batch data from June 1, 2024 to target date"""
    start_date = datetime.strptime(start, "%Y-%m-%d")
    T = datetime(2025, 12, 26)

    batches = {}
    d = start_date
    while d <= T:
        count = random.randint(6, 20)
        daily_reviews = random.sample(REVIEW_POOL, k=min(count, len(REVIEW_POOL)))
        # inject a few random evolving topics
        if random.random() > 0.5:
            daily_reviews.append(f"Evolving feedback #{random.randint(100,9999)}")
        batches[d.strftime("%Y-%m-%d")] = daily_reviews
        d += timedelta(days=1)

    logging.info(f"Loaded {len(batches)} daily batches")
    return batches
