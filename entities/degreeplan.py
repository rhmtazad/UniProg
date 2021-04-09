from repository import EntityCollection


class DegreePlan:
    def __init__(self, database, major):
        self.__degree_plan = EntityCollection(database, major)

    def remove_prop(self, major, **prop):
        self.__degree_plan.remove_attribute(major, **prop)
