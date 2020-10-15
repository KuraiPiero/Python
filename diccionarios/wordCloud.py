from wordcloud import WordCloud, STOPWORDS
import wikipedia
import os
from PIL import Image
import numpy as np

stop_words = [
    "el",
    "la",
    "un",
    "una",
    "ella",
    "ellos",
    "en",
    "unos",
    "yo",
    "tu",
    "nosotros",
    "vosotros",
    "con",
    "del",
    "es",
    "la",
    "lo",
    "por",
    "los",
    "se",
    "las",
    "mas",
    "más",
    "al",
    "que",
    "de",
    "ISBN",
    "sino" "para",
    "otro",
    "esta",
    "entre",
    "otro",
    "su",
] + list(STOPWORDS)


cur_dir = os.path.dirname(__file__)


def get_wiki(query):
    wikipedia.set_lang("es")
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content


def create_word_cloud_img(text):
    mask = np.array(Image.open(os.path.join(cur_dir, "mask.png")))
    wc = WordCloud(background_color="white", mask=mask, max_words=200, stopwords=stop_words)
    wc.generate(text)
    wc.to_file(os.path.join(cur_dir, "image.png"))


create_word_cloud_img(get_wiki("Poesia"))
