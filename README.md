## UniProg v3.1.1

[![Software Engineering - Scrum Project](https://img.shields.io/badge/Software_Engineering-Scrum_Project-important)](https://github.com/rhmtazad/UniProg/) 
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org) 
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

## User Interface Preview

### Dahboard  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/dashboard.JPG"/>  


### Degree Plan Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/degreeplan.JPG"/>  


### Account Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/account.JPG"/>  


## Requirements

**To use this software you must have installed:**
- [Python 3.9] - Latest version of Python
- [SQLite3] - Latest version of SQLite3

## Installation

**After finishing this project a single-executable file will be realease**

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
student_data = [ 38786, 'Rahmat', 'Azad', 'me@gmail.com', 'rhmtazad', 'eyePatch', 'Dr. Ala', 'ala@gmail.com']
```


```python
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

```


```python
courses_csv = CSVFile(columns=course_columns, index='id', file='courses')
```


```python
courses = pd.DataFrame(courses_csv.read(), columns=courses_csv.columns).set_index(courses_csv.index)
```


```python
courses
```




<div>
<table>
  <thead>
    <tr>
      <th></th>
      <th>name</th>
      <th>category</th>
      <th>credits</th>
      <th>taken</th>
      <th>grade</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
degreeplan_csv = CSVFile(columns=degreeplan_columns, index='major', file='degreeplan')
```


```python
degreeplan = pd.DataFrame(degreeplan_csv.read(), columns=degreeplan_csv.columns).set_index(degreeplan_csv.index)
```


```python
degreeplan
```




<div>
<table>
  <thead>
    <tr>
      <th></th>
      <th>year</th>
      <th>conc</th>
      <th>credits</th>
      <th>courses</th>
      <th>gen_credits</th>
      <th>core_credits</th>
      <th>conc_credits</th>
    </tr>
    <tr>
      <th>major</th>
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
  </tbody>
</table>
</div>




```python
student_csv = CSVFile(columns=student_columns, index='id', file='student')
```


```python
student = pd.DataFrame(student_csv.read(), columns=student_csv.columns).set_index(student_csv.index)
```


```python
student
```

<div>
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
  </tbody>
</table>
</div>


## Scrum Master and Product Owner

- Fatema Qambari (Product Owner)
- Nasrin Natiqi  (Scrum Master)

## Developer Team

- Rahmat Azad
- Mohammad Sulayman Rezaie
- Sajjad Afzali
- Tasal Sahibzadah
