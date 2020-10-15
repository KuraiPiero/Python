import wordcloud
import wikipedia


def get_words(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content


print(get_words("Belleza"))
