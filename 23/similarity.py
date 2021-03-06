import os
import re
from difflib import SequenceMatcher
import itertools
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

try:
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
        TEMPFILE
    )
except FileNotFoundError:
    TEMPFILE = "feed"


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # do your thing ...

    similarTagPairs = []
    tags = list(tags)

    for i in range(len(tags)-1):
        tag1 = tags[i]
        if len(tag1) < MIN_TAG_LEN:
            continue
        for j in range(i+1, len(tags)):
            tag2 = tags[j]
            if len(tag2) < MIN_TAG_LEN:
                continue
            s = SequenceMatcher(
                    lambda x: x==" ",
                    tag1,
                    tag2
                    )
            similarity = s.ratio()
            if similarity >= SIMILAR:
                similarTagPairs.append((tag1, tag2))

    return similarTagPairs

