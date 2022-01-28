import sys
sys.path.append('../..')

import re


def prettify_json(text, indent=2, collapse_level=4):
    pattern = r"[\r\n]+ {%d,}" % (indent * collapse_level)
    text = re.sub(pattern, ' ', text)
    text = re.sub(r'([\[({])+ +', r'\g<1>', text)
    text = re.sub(r'[\r\n]+ {%d}([])}])' % (indent * (collapse_level-1)), r'\g<1>', text)
    text = re.sub(r'(\S) +([])}])', r'\g<1>\g<2>', text)
    return text
