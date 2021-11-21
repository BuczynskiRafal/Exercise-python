class HouseProject:
    number_of_floors = 3
    area = 100

    def describe_project():
        print(f"Floor number: {HouseProject.number_of_floors}")
        print(f"Area: {HouseProject.area}")


print(HouseProject.describe_project())