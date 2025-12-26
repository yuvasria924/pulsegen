import pandas as pd
from datetime import datetime, timedelta
from collections import Counter
from agent_core import extract_topics, consolidate_topics

def build_trend_table(batches, T_date):
    """Build trend table from T-30 to T"""
    T = datetime.strptime(T_date, "%Y-%m-%d")
    start = T - timedelta(days=30)

    all_topics = []
    for date, reviews in batches.items():
        d = datetime.strptime(date, "%Y-%m-%d")
        if start <= d <= T:
            all_topics += extract_topics(reviews)

    topics = consolidate_topics(all_topics)

    report_rows = []
    for topic in topics:
        row = {"Topic": topic}
        for i in range(30, -1, -1):
            date = (T - timedelta(days=i)).strftime("%Y-%m-%d")
            day_reviews = batches.get(date, [])
            day_topics = extract_topics(day_reviews)
            freq = Counter(day_topics).get(topic, 0)
            row[date] = freq
        report_rows.append(row)

    return pd.DataFrame(report_rows)
