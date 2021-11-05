class Container:
    @classmethod
    def show_details(cls):
        print(f"Running from {cls.__name__} class.")


container = Container()
container.show_details()
