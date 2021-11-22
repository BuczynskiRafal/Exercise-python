class Hashtag:

    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Hashtag(self.string[1:] + ' ' + other.string)


hashtag1 = Hashtag('python')
hashtag2 = Hashtag('developer')
hashtag3 = Hashtag('oop')
print(hashtag1 + hashtag2 + hashtag3)