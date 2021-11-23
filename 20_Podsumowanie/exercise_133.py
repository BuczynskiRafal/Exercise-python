import time


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime())


note1 = Note('My first note.')
note2 = Note('My second note.')
