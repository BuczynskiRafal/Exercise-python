def clean_hashtags():
    with open('hashtags.txt', 'r') as file:
        text = file.readlines()
        print(text)


print(clean_hashtags())
