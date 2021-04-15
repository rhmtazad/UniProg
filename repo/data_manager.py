import pandas as pd
from dataclasses import dataclass, field


@dataclass(order=True)
class CSVFile:
    index: str
    file: str
    columns: list[str] = field(default_factory=list)
        
    def __post_init__(self):
        self.save(self.columns_df)

    @property
    def columns_df(self):
        return pd.DataFrame(columns=self.columns).set_index(self.index)

    def data_df(self, data):
        return pd.DataFrame([data], columns=self.columns).set_index(self.index)

    def read(self):
        return pd.read_csv(f'{self.file}.csv', index_col=self.index)

    def save(self, indexed_df):
        indexed_df.to_csv(f'{self.file}.csv')

    def insert(self, data):
        self.save(self.read().append(self.data_df(data)))


course_columns = ['id', 'name', 'category', 'credits', 'taken', 'grade']
course_data = ['ITC 315', 'Software Engineering', 'Concentration', 3, 'True', 'A']

degreeplan_columns = ['major', 'year', 'conc', 'credits', 'courses', 'gen_credits', 'core_credits', 'conc_credits']
degreeplan_data = ['Information Technology', '2018', 'Software Engineering', 120, 40, 60, 51, 9]

student_columns = ['id', 'name', 'lastname', 'email', 'username', 'password', 'advisor', 'advisor_email']
student_data = [ 38786, 'Rahmat', 'Azad', 'me@gmail.com', 'rhmtazad', 'eyePatch', 'Dr. Ala', 'ala@gmail.com']


courses_csv = CSVFile(columns=course_columns, index='id', file='courses')
courses = pd.DataFrame(courses_csv.read(), columns=courses_csv.columns).set_index(courses_csv.index)

degreeplan_csv = CSVFile(columns=degreeplan_columns, index='major', file='degreeplan')
degreeplan = pd.DataFrame(degreeplan_csv.read(), columns=degreeplan_csv.columns).set_index(degreeplan_csv.index)

student_csv = CSVFile(columns=student_columns, index='id', file='student')
student = pd.DataFrame(student_csv.read(), columns=student_csv.columns).set_index(student_csv.index)