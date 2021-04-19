import math

from repo.csv_file import CSVFile
import pandas as pd


class Courses:
    __slots__ = ['file']

    def __init__(self):
        self.file = CSVFile(index=self.columns[0], file='courses', columns=self.columns)

    @property
    def columns(self):
        return [
            'id',
            'name',
            'category',
            'credits',
            'taken',
            'grade'
        ]

    def save(self, course_info):
        self.file.insert(course_info[0], course_info)

    def update(self, course_info, old_index):
        self.file.update(course_info[0], course_info, old_index)

    def delete(self, index):
        self.file.drop(index)

    @staticmethod
    def read():
        return pd.read_csv('courses.csv').sort_values(by='id', ascending=True).values.tolist()

    @staticmethod
    def search(value, column):
        df = pd.read_csv('courses.csv', dtype=str)
        return df[df[column].str.contains(value)].values.tolist()

    def group_courses(self):
        return self.file.read().groupby(['category', 'taken']).size()

    @property
    def gen_status(self):
        return dict(self.group_courses().General)

    @property
    def conc_status(self):
        return dict(self.group_courses().Concentration)

    @property
    def core_status(self):
        return dict(self.group_courses().Core)

    @property
    def taken_status(self):
        return dict(self.file.read().groupby(['taken']).size())

    @property
    def remaining_semesters(self):
        return math.ceil(int(self.taken_status['False']) / 5)

    @property
    def gpa(self):
        return str(pd.read_csv('courses.csv')['grade'].mean().round(2))
