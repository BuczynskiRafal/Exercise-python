import time


class Container:
    @staticmethod
    def get_current_time():
        return str(time.ctime().split()[3])


print(Container.get_current_time())
