# import time
#
#
# class Container:
#
#     @staticmethod
#     def get_current_time():
#         return str(time.ctime().split()[3])
#
#
# print(Container.get_current_time())


import time


class Container:

    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())

    get_current_time = staticmethod(get_current_time)