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
from dataclasses import dataclass, field


@dataclass(order=True)
class UniProgCSV:
    index: str
    file: str
    columns: list[str] = field(default_factory=list)

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


