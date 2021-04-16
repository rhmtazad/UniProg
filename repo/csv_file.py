import pathlib
from dataclasses import dataclass, field

import pandas as pd


@dataclass(order=True)
class CSVFile:
    index: str
    file: str
    columns: list[str] = field(default_factory=list)

    def __post_init__(self):
        if pathlib.Path(f'{self.file}.csv').exists():
            pass
        else:
            self.save(self.columns_df)

    @property
    def columns_df(self):
        return pd.DataFrame(columns=self.columns).set_index(self.index)

    def make_series(self, row):
        series_dict = dict(zip(self.columns, row))
        return pd.Series(series_dict, name=series_dict[self.index]).drop(labels=self.index)

    def read(self):
        return pd.read_csv(f'{self.file}.csv', index_col=self.index)

    def save(self, indexed_df):
        indexed_df.to_csv(f'{self.file}.csv')

    def drop(self, name):
        df = self.read()
        if name in df.index:
            self.save(df.drop(name))

    def insert(self, row):
        series = self.make_series(row)
        df = self.read()
        if series.name in df.index:
            df = df.drop(series.name)
            self.save(df.append(series))
        else:
            self.save(df.append(series))

    def update(self, row, old_index):
        self.insert(row)
        self.drop(old_index)

    def get(self, index, column):
        return str(self.read().loc[index][f'{column}'])


course_columns = ['id', 'name', 'category', 'credits', 'taken', 'grade']
course1 = ['ITC 315', 'Software Engineering', 'Concentration', 3, 'True', 'A']

degreeplan_columns = ['major', 'year', 'conc', 'credits', 'courses', 'gen_credits', 'core_credits', 'conc_credits']
degreeplan1 = ['Information Technology', '2018', 'Software Engineering', 120, 40, 60, 51, 9]

student_columns = ['id', 'name', 'lastname', 'email', 'username', 'password', 'advisor', 'advisor_email']
student1 = [38788, 'A', 'B', 'a@gmail.com', 'eyePatchA', 'eyePatch1', 'AB', 'ab@gmail.com']
student2 = [40048, 'B', 'C', 'b@gmail.com', 'eyePatchB', 'eyePatch2', 'BC', 'bc@gmail.com']
student3 = [48400, 'C', 'D', 'c@gmail.com', 'eyePatchC', 'eyePatch3', 'CD', 'cd@gmail.com']
student4 = [38786, 'D', 'E', 'd@gmail.com', 'eyePatchD', 'eyePatch4', 'DE', 'de@gmail.com']
student5 = [38789, 'E', 'F', 'e@gmail.com', 'eyePatchE', 'eyePatch5', 'EF', 'ef@gmail.com']

student = CSVFile(index='id', file='student', columns=student_columns)
course = CSVFile(index='id', file='course', columns=course_columns)
degreeplan = CSVFile(index='major', file='degreeplan', columns=degreeplan_columns)

student.insert(student1)
student.insert(student2)
student.insert(student3)
student.insert(student4)
student.insert(student5)
student.read()

student.update(student5, 38786)
student.read()

student_df = pd.DataFrame(student.read(), columns=student.columns[1:])

student.get(38786, 'name')
