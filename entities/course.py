from repository import Record


class Course:
    def __init__(self, database):
        self.course = Record(database)

    def add(self, major, **data):
        self.course.add(major, **data)

    def remove(self, major, course_id):
        self.course.remove(major, course_id)

    def update(self, major, course_id, **data):
        self.course.update(major, course_id, **data)

    def prop(self, major, course_id, prop):
        return self.course.attribute(major, course_id, prop)

    def get(self, major, course_id):
        return self.course.get(major, course_id)

    def filter(self, major, course_id, *prop):
        return self.course.filter(major, course_id, *prop)

    def count(self, major, **property_value):
        return self.course.count(major, **property_value)
