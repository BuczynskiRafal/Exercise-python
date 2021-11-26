class CustomDict(dict):

    def is_any_str_value(self):
        for k in self:
            if isinstance(self[k], str):
                return True
            else:
                return False


cd = CustomDict(python=1)
print(cd.is_any_str_value())