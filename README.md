## UniProg v3.1.1

[![Software Engineering - Scrum Project](https://img.shields.io/badge/Software_Engineering-Scrum_Project-important)](https://github.com/rhmtazad/UniProg/) 
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
[![stars - uniprog](https://img.shields.io/github/stars/rhmtazad/uniprog?style=social)](https://github.com/rhmtazad/uniprog) 
[![forks - uniprog](https://img.shields.io/github/forks/rhmtazad/uniprog?style=social)](https://github.com/rhmtazad/uniprog) 

### A GUI Tool Kit for Students to Manage their Degree Plan and Courses

```
This project is originally developed for our Software Engineering Course.
The intention of this project to practice the software development life-cycle, software development 
practices, and different but related methodologies. 
The Scrum model suggests that projects progress via a series of sprints.  
In keeping with an agile methodology, sprints are timeboxed to 
no more than a month long, most commonly two weeks.

Scrum methodology advocates for a planning meeting at the start of the sprint,
where team members figure out how many items they can commit to, 
and then create a sprint backlog – a list of the tasks to perform during the sprint.  
```

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
import pandas as pd
```


```python
course_columns = [
    'id',
    'name',
    'category',
    'credits',
    'taken',
    'grade'
]

course_data = [
    'ITC 315',
    'Software Engineering',
    'Concentration',
    3,
    'True',
    'A'
]
```


```python
degreeplan_columns = [
    'major',
    'year',
    'concentration',
    'total_credits',
    'total_courses',
    'general_credits',
    'core_credits',
    'concentration_credits'
]

degreeplan_data = [
    'Information Technology',
    '2018',
    'Software Engineering',
    120, 40, 60, 51, 9
]
```


```python
student_columns = [
    'id',
    'name',
    'lastname',
    'email',
    'username',
    'password',
    'advisor',
    'advisor_email'
]

student_data = [
    38786,
    'Rahmat',
    'Azad',
    'rahmat.azad@auaf.edu.af',
    'rhmtazad',
    'eyePatch17',
    'Dr. Ala Abdulhakim Abdulaziz',
    'ala@auaf.edu.af'
]
```


```python
class UniProgCSV:
    def __init__(self, columns, index, file):
        self.columns = columns
        self.index = index
        self.file = file

    @property
    def columns_df(self):
        return pd.DataFrame(columns=self.columns).set_index(self.index)

    def data_df(self, data):
        return pd.DataFrame([data], columns=self.columns).set_index(self.index)

    def read(self):
        try:
            return pd.read_csv(f'{self.file}.csv', index_col=self.index)
        except FileNotFoundError:
            self.save(self.columns_df)
            return pd.read_csv(f'{self.file}.csv', index_col=self.index)

    def save(self, indexed_df):
        indexed_df.to_csv(f'{self.file}.csv')

    def append(self, data):
        self.save(self.read().append(self.data_df(data)))
```


```python
courses = UniProgCSV(columns=course_columns, index='id', file='courses')
```


```python
courses.columns
```




    ['id', 'name', 'category', 'credits', 'taken', 'grade']




```python
courses.columns_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
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
courses.read()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
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
    <tr>
      <th>ITC 315</th>
      <td>Software Engineering</td>
      <td>Concentration</td>
      <td>3</td>
      <td>True</td>
      <td>B+</td>
    </tr>
    <tr>
      <th>ITC 315</th>
      <td>Software Engineering</td>
      <td>Concentration</td>
      <td>3</td>
      <td>True</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>




```python
courses.append(course_data)
```


```python
courses.read()
```



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
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
    <tr>
      <th>ITC 315</th>
      <td>Software Engineering</td>
      <td>Concentration</td>
      <td>3</td>
      <td>True</td>
      <td>B+</td>
    </tr>
    <tr>
      <th>ITC 315</th>
      <td>Software Engineering</td>
      <td>Concentration</td>
      <td>3</td>
      <td>True</td>
      <td>A</td>
    </tr>
    <tr>
      <th>ITC 315</th>
      <td>Software Engineering</td>
      <td>Concentration</td>
      <td>3</td>
      <td>True</td>
      <td>A</td>
    </tr>
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
