import re
from typing import List

__all__ = ["replace_punctuation", "tokenize_by_cjk_char"]

_punctuation = r"[,\.?!\"，。？！“”：:、<>《》\[\]{}【】;；]"

def replace_punctuation(text: str, replacement: str = "") -> str:
    return re.sub(_punctuation, replacement, text)


def tokenize_by_cjk_char(text: str, remove_punctuation: bool = True, merge_cjk: bool = False) -> List[str]:
    text = text.strip()
    puncs = re.compile(_punctuation)

    if remove_punctuation:
        text = replace_punctuation(text, " ")

    pattern = re.compile(
        r"([\u1100-\u11ff\u2e80-\ua4cf\ua840-\uD7AF\uF900-\uFAFF\uFE30-\uFE4F\uFF65-\uFFDC\U00020000-\U0002FFFF])"
    )
    
    chars = pattern.split(text)
    words: List[str] = []
    for w in chars:
        if w.strip():
            if merge_cjk and (pattern.match(w) or puncs.match(w)):
                if words and (pattern.match(words[-1]) or puncs.match(words[-1])):
                    words[-1] += w
                else:
                    words.append(w)
            else:
                words.extend(w.split())
    return words