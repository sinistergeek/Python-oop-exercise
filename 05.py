import time
class Container:
    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())


current_time = Container.get_current_time()
print(current_time)
