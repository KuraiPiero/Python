def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        texts = word[1:] + word[0] + "ay" + " "
        say += texts
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"

print(
    pig_latin("programming in python is fun")
)  # Should be "rogrammingpay niay ythonpay siay unfay"

