class Worker:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"{self.__class__.__name__}(fname='{self.fname}', lname='{self.lname}')"


worker = Worker('Mike', 'Smith')

print(worker)