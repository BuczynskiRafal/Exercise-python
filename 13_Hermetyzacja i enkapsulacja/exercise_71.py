class TechStack:

    def __init__(self, tech_names):
        self.tech_names = tech_names

    @property
    def tech_names(self):
        return self._tech_names

    @tech_names.setter
    def tech_names(self, tech):
        self._tech_names = tech

    @tech_names.deleter
    def tech_names(self):
        del self._tech_names


tech_stack = TechStack('python,java,sql')
print(tech_stack.tech_names)
tech_stack.tech_names = 'python,java'
print(tech_stack.tech_names)
del tech_stack.tech_names
print(tech_stack.__dict__)

