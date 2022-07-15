import itertools


def clean_hashtags():
    with open('hashtags.txt', 'r') as file:
        text = file.readlines()
    return sorted(list(set([word.replace('/n', '') for sublist in text for word in sublist.split() if len(word) <= 5])))



print(clean_hashtags())
