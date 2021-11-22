class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __lt__(self, other):
        return len(self.string) < len(other.string)


doc1 = Doc('sport')
doc2 = Doc('activity')
print(doc1 < doc2)