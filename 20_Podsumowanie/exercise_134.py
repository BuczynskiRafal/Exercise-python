import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    def find(self, word):
        return word in self.content


note1 = Note('Object Oriented Programing in Python.')
print(note1.find('python'))
print(note1.find('Python'))