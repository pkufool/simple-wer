import re
from typing import List

__all__ = ["replace_punctuation", "tokenize_by_cjk_char"]

_punctuation = r"[,\.?!\"，。？！""：:、<>《》\[\]{}【】;；]"


def replace_punctuation(text: str, replacement: str = "") -> str:
    """Replace punctuation characters in text.

    Matches the following punctuation characters:
        , . ? ! " ， 。 ？ ！ " " ： : 、 < > 《 》 [ ] { } 【 】 ; ；

    Args:
      text:
        Input text.
      replacement:
        String to replace each punctuation character with.
        Defaults to "" (remove punctuation).

    Returns:
      Text with punctuation replaced.
    """
    return re.sub(_punctuation, replacement, text)


def tokenize_by_cjk_char(text: str, remove_punctuation: bool = True, merge_cjk: bool = False) -> List[str]:
    """Tokenize text by splitting CJK characters into individual tokens.

    Non-CJK words (e.g. English) are kept intact. CJK characters are
    split into one character per token by default, or merged into
    consecutive groups when ``merge_cjk=True``.

    The CJK ranges covered are:
      - Hangul Jamo:             U+1100 - U+11FF
      - CJK Radicals / Kangxi:   U+2E80 - U+2FDF
      - CJK Symbols & Punctuation / Ideographs: U+3000 - U+9FFF
      - Hangul Syllables:        U+AC00 - U+D7AF
      - CJK Compatibility Ideographs: U+F900 - U+FAFF
      - CJK Compatibility Forms:  U+FE30 - U+FE4F
      - Halfwidth CJK Punctuation: U+FF65 - U+FFDC
      - CJK Extension B:         U+20000 - U+2FFFF

    Args:
      text:
        Input text. Can contain mixed CJK and non-CJK scripts.
      remove_punctuation:
        If True (default), punctuation is removed (replaced with spaces)
        before tokenization.
        If False, punctuation acts as a word boundary and is preserved as
        a separate token in the output.
      merge_cjk:
        If True, consecutive CJK characters are merged into a single token
        instead of being split individually. Non-CJK words are unaffected.

    Returns:
      A list of tokens.

    Examples:
      Given text: "你好，hello world！世界"

      1. remove_punctuation=True (default), merge_cjk=False (default):

      >>> tokenize_by_cjk_char("你好，hello world！世界")
      ['你', '好', 'hello', 'world', '世', '界']

      2. remove_punctuation=True, merge_cjk=True:

      >>> tokenize_by_cjk_char("你好，hello world！世界", merge_cjk=True)
      ['你好', 'hello', 'world', '世界']

      3. remove_punctuation=False, merge_cjk=False:

      >>> tokenize_by_cjk_char("你好，hello world！世界", remove_punctuation=False)
      ['你', '好', '，', 'hello', 'world', '！', '世', '界']

      4. remove_punctuation=False, merge_cjk=True:

      >>> tokenize_by_cjk_char("你好，hello world！世界", remove_punctuation=False, merge_cjk=True)
      ['你好，', 'hello', 'world！', '世界']
    """
    text = text.strip()
    puncs = re.compile(_punctuation)

    if remove_punctuation:
        text = replace_punctuation(text, " ")
    else:
        text = puncs.sub(r" \g<0> ", text)

    pattern = re.compile(
        r"([\u1100-\u11ff\u2e80-\ua4cf\ua840-\uD7AF\uF900-\uFAFF\uFE30-\uFE4F\uFF65-\uFFDC\U00020000-\U0002FFFF])"
    )

    chars = pattern.split(text)
    words: List[str] = []
    for w in (w for item in chars for w in item.split()):
        is_cjk = pattern.match(w)
        is_punc = puncs.match(w)
        prev_is_cjk = words and (pattern.match(words[-1]) or puncs.match(words[-1]))
        if merge_cjk and words and (is_punc or (is_cjk and prev_is_cjk)):
            words[-1] += w
        else:
            words.append(w)
    return words
