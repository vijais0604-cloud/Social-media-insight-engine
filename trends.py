import re
from collections import Counter

HASHTAG_RE = re.compile(r"#\w+")

def extract_hashtags(texts):
    tags = []
    for t in texts:
        tags.extend(HASHTAG_RE.findall(t.lower()))
    return Counter(tags).most_common(10)

