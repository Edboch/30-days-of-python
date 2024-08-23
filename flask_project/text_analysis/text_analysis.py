from collections import Counter
import regex
from lexical_diversity import lex_div as ld

def most_appearing_word(words:list[str]):
    return Counter(words).most_common(1)[0][0]

def all_word_count(words:list[str]):
    return Counter(words).most_common()

def clean_text(text:str):
    pattern = r'[^\w\s]'
    cleaned = regex.sub(pattern,'',text)
    return cleaned

def lex_density(words:str):
    lex = ld.flemmatize(words)
    return round(ld.ttr(lex) * 100,1)

