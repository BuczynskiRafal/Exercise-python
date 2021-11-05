class Container:
    @classmethod
    def show_details(cls):
        print(f"Running from {__class__.__name__} class")


print(Container.show_details())
