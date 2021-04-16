## UniProg v3.1.2

[![Software Engineering - Scrum Project](https://img.shields.io/badge/Software_Engineering-Scrum_Project-important)](https://github.com/rhmtazad/UniProg/) 
[![Made with Python](https://img.shields.io/badge/Python->=3.7-blue?logo=python&logoColor=white)](https://python.org) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
[![stars - uniprog](https://img.shields.io/github/stars/rhmtazad/uniprog?style=social)](https://github.com/rhmtazad/uniprog) 
[![forks - uniprog](https://img.shields.io/github/forks/rhmtazad/uniprog?style=social)](https://github.com/rhmtazad/uniprog) 

### A GUI Tool Kit for Students to Manage their Degree Plan and Courses

___  

This project is originally developed for our Software Engineering Course.
The intention of this project to practice the software development life-cycle, software development 
practices, and different but related methodologies. 
The Scrum model suggests that projects progress via a series of sprints.  
In keeping with an agile methodology, sprints are timeboxed to 
no more than a month long, most commonly two weeks.

Scrum methodology advocates for a planning meeting at the start of the sprint,
where team members figure out how many items they can commit to, 
and then create a sprint backlog – a list of the tasks to perform during the sprint.  
___  


## Scrum Master and Product Owner

- Fatema Qambari (Product Owner)
- Nasrin Natiqi  (Scrum Master)

## Developer Team

- Rahmat Azad
- Mohammad Sulayman Rezaie
- Sajjad Afzali
- Tasal Sahibzadah

## User Interface Preview

### Dashboard  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/dashboard.JPG"/>  


### Degree Plan Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/degreeplan.JPG"/>  


### Account Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/account.JPG"/>  


### Courses Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/courses.JPG"/>  


## Requirements

**To use this software you must have installed:**
- [Python 3.9] - Latest version of Python
- [SQLite3] - Latest version of SQLite3

## Installation

**After finishing this project a single-executable file will be released**

```
This part is intentionally left blank...
```

## How to Use Jupyter Notebook

```python
course_columns = ['id', 'name', 'category', 'credits', 'taken', 'grade']
```


```python
course_data = ['ITC 315', 'Software Engineering', 'Concentration', 3, 'True', 'A']
```


```python
degreeplan_columns = ['major', 'year', 'conc', 'credits', 'courses', 'gen_credits', 'core_credits', 'conc_credits']
```


```python
degreeplan_data = ['Information Technology', '2018', 'Software Engineering', 120, 40, 60, 51, 9]
```


```python
student_columns = ['id', 'name', 'lastname', 'email', 'username', 'password', 'advisor', 'advisor_email']
```


```python
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
```


```python
student = CSVFile(index='id', file='student', columns=student_columns)
```


```python
student1 = [38788, 'A', 'B', 'a@gmail.com', 'eyePatchA', 'eyePatch1', 'AB', 'ab@gmail.com']
student2 = [40048, 'B', 'C', 'b@gmail.com', 'eyePatchB', 'eyePatch2', 'BC', 'bc@gmail.com']
student3 = [48400, 'C', 'D', 'c@gmail.com', 'eyePatchC', 'eyePatch3', 'CD', 'cd@gmail.com']
student4 = [38786, 'D', 'E', 'd@gmail.com', 'eyePatchD', 'eyePatch4', 'DE', 'de@gmail.com']
student5 = [38789, 'E', 'F', 'e@gmail.com', 'eyePatchE', 'eyePatch5', 'EF', 'ef@gmail.com']
```


```python
student.insert(student1)
student.insert(student2)
student.insert(student3)
student.insert(student4)
student.insert(student5)
student.read()
```

<table>
  <thead>
    <tr>
      <th></th>
      <th>name</th>
      <th>lastname</th>
      <th>email</th>
      <th>username</th>
      <th>password</th>
      <th>advisor</th>
      <th>advisor_email</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40048</th>
      <td>B</td>
      <td>C</td>
      <td>b@gmail.com</td>
      <td>eyePatchB</td>
      <td>eyePatch2</td>
      <td>BC</td>
      <td>bc@gmail.com</td>
    </tr>
    <tr>
      <th>48400</th>
      <td>C</td>
      <td>D</td>
      <td>c@gmail.com</td>
      <td>eyePatchC</td>
      <td>eyePatch3</td>
      <td>CD</td>
      <td>cd@gmail.com</td>
    </tr>
    <tr>
      <th>38786</th>
      <td>D</td>
      <td>E</td>
      <td>d@gmail.com</td>
      <td>eyePatchD</td>
      <td>eyePatch4</td>
      <td>DE</td>
      <td>de@gmail.com</td>
    </tr>
    <tr>
      <th>38788</th>
      <td>E</td>
      <td>F</td>
      <td>e@gmail.com</td>
      <td>eyePatchE</td>
      <td>eyePatch5</td>
      <td>EF</td>
      <td>ef@gmail.com</td>
    </tr>
  </tbody>
</table>
</div>




```python
student.update(student5, 38786)
student.read()
```

<table>
  <thead>
    <tr>
      <th></th>
      <th>name</th>
      <th>lastname</th>
      <th>email</th>
      <th>username</th>
      <th>password</th>
      <th>advisor</th>
      <th>advisor_email</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40048</th>
      <td>B</td>
      <td>C</td>
      <td>b@gmail.com</td>
      <td>eyePatchB</td>
      <td>eyePatch2</td>
      <td>BC</td>
      <td>bc@gmail.com</td>
    </tr>
    <tr>
      <th>48400</th>
      <td>C</td>
      <td>D</td>
      <td>c@gmail.com</td>
      <td>eyePatchC</td>
      <td>eyePatch3</td>
      <td>CD</td>
      <td>cd@gmail.com</td>
    </tr>
    <tr>
      <th>38788</th>
      <td>E</td>
      <td>F</td>
      <td>e@gmail.com</td>
      <td>eyePatchE</td>
      <td>eyePatch5</td>
      <td>EF</td>
      <td>ef@gmail.com</td>
    </tr>
    <tr>
      <th>38789</th>
      <td>E</td>
      <td>F</td>
      <td>e@gmail.com</td>
      <td>eyePatchE</td>
      <td>eyePatch5</td>
      <td>EF</td>
      <td>ef@gmail.com</td>
    </tr>
  </tbody>
</table>
</div>




```python
student_df = pd.DataFrame(student.read(), columns=student.columns[1:])
student_df
```


<table>
  <thead>
    <tr>
      <th></th>
      <th>name</th>
      <th>lastname</th>
      <th>email</th>
      <th>username</th>
      <th>password</th>
      <th>advisor</th>
      <th>advisor_email</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40048</th>
      <td>B</td>
      <td>C</td>
      <td>b@gmail.com</td>
      <td>eyePatchB</td>
      <td>eyePatch2</td>
      <td>BC</td>
      <td>bc@gmail.com</td>
    </tr>
    <tr>
      <th>48400</th>
      <td>C</td>
      <td>D</td>
      <td>c@gmail.com</td>
      <td>eyePatchC</td>
      <td>eyePatch3</td>
      <td>CD</td>
      <td>cd@gmail.com</td>
    </tr>
    <tr>
      <th>38786</th>
      <td>D</td>
      <td>E</td>
      <td>d@gmail.com</td>
      <td>eyePatchD</td>
      <td>eyePatch4</td>
      <td>DE</td>
      <td>de@gmail.com</td>
    </tr>
    <tr>
      <th>38788</th>
      <td>E</td>
      <td>F</td>
      <td>e@gmail.com</td>
      <td>eyePatchE</td>
      <td>eyePatch5</td>
      <td>EF</td>
      <td>ef@gmail.com</td>
    </tr>
  </tbody>
</table>
</div>




```python
student.get(38786, 'name')
```




    'D'


