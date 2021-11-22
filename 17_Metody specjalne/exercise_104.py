class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __iadd__(self, other):
        return self.string + ' &amp; ' + other.string

doc1 = Doc('sport')
doc2 = Doc('activity')

doc1 += doc2

print(doc1)