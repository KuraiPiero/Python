def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        n = sentence.split()
        i = sentence.index(old, int(-(len(sentence) / 2.5)))
        n.pop()
        n.append(new)
        new_sentence = " ".join(n)
        return new_sentence
    else:
        return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
