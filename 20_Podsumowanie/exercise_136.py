import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    def __repr__(self):
        return f"Note(content='{self.content}')"

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook(Note):

    def __init__(self):
        self.notes = []

    def new_note(self, note):
        self.notes.append(Note(note))


notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
print(notebook.notes)
